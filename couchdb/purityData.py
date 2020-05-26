# Author: Minshen Lu
# ID : 1039243
# Team : 32

import json
from textblob import TextBlob
from mpi4py import MPI


def IsPtInPoly(aLon, aLat, pointList):
    iSum = 0
    iCount = len(pointList)
    if iCount < 3:
        return False
    for i in range(iCount):
        pLon1 = pointList[i][0]
        pLat1 = pointList[i][1]
        if i == iCount - 1:
            pLon2 = pointList[0][0]
            pLat2 = pointList[0][1]
        else:
            pLon2 = pointList[i + 1][0]
            pLat2 = pointList[i + 1][1]
        if ((aLat >= pLat1) and (aLat < pLat2)) or ((aLat >= pLat2) and (aLat < pLat1)):
            if abs(pLat1 - pLat2) > 0:
                pLon = pLon1 - ((pLon1 - pLon2) * (pLat1 - aLat)) / (pLat1 - pLat2);
                if pLon < aLon:
                    iSum += 1

    if iSum % 2 != 0:
        return True
    else:
        return False


def Core():
    FILE_PATH_IMPORT = '/Volumes/Samsung_T5/twitter-2017.json'
    LOCATION_LIST_PATH = '/Users/luminshen/Documents/代码/PycharmProjects/A2_/couchdb/vic_geo.json'
    suburbs_list = open(LOCATION_LIST_PATH)
    suburbs_list = json.load(suburbs_list)['features']

    month = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
             'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    result = ""
    with open(FILE_PATH_IMPORT) as file:
        is_reported = True
        i = 0  # 实际新增数据
        set_ = set()  # 新增的 suburbs 数目
        print('进程{} 处理中...'.format(rank))
        for index_, line in enumerate(file):
            if index_ % size == rank:
                if index_ == 0:
                    continue
                try:
                    if i % 300 == 0 and is_reported is False:
                        print("进程{} 已经新增了 {} 条数据".format(rank, i))
                        is_reported = True
                    doc = json.loads(line[:-2])
                    if ('doc' not in doc) or (len(doc['doc']['entities']['hashtags']) == 0):
                        continue

                    tmp_line = {'doc': {}}

                    # 处理情感👇 sentiments_exact: 储存具体数值; sentiments_booleant: 储存-1,0,1
                    blob = TextBlob(doc['doc']['text'])
                    sentiment = blob.sentiment[0]
                    tmp_line['doc']['sentiments_exact'] = sentiment
                    if sentiment > 0:
                        sentiment = 1
                    elif sentiment < 0:
                        sentiment = -1
                    else:
                        sentiment = int(sentiment)
                    tmp_line['doc']['sentiments_boolean'] = sentiment
                    # 处理情感👆

                    # 处理 hashtags👇
                    hashtags = doc['doc']['entities']['hashtags']
                    tmp_line['doc']['hashtags'] = []
                    for hashtag in hashtags:
                        tmp_line['doc']['hashtags'].append(hashtag['text'].lower())
                    # 处理 hashtags👆

                    # 处理 时间👇
                    time = doc['doc']['created_at'].split(" ")
                    time = int(time[-1] + month[time[1]] + time[2])
                    tmp_line['doc']['timestamp'] = time
                    # 处理 时间👆

                    # 处理坐标字段👇
                    [x, y] = doc['doc']['coordinates']['coordinates']
                    for suburb in suburbs_list:
                        polygon = suburb['geometry']['coordinates'][0]
                        if IsPtInPoly(x, y, polygon):
                            tmp_line['doc']['location'] = suburb['properties']['vic_loca_2']
                            set_.add(tmp_line['doc']['location'])
                            break
                        else:
                            continue
                    # 处理坐标字段👆

                    i += 1
                    is_reported = False
                    result += str(tmp_line) + '\n'
                except:
                    continue
    return result, i


if __name__ == '__main__':
    LOG_PATH = '/Users/luminshen/Desktop/CCC/log.txt'
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    # print("size: ", size, 'rank: ', rank)
    data = Core()
    data = comm.gather(data, root=0)
    if rank == 0:
        i = 0
        FILE_PATH_OUTPUT = '/Users/luminshen/Desktop/CCC/twitter-data/twitter-2017-processed.json'
        file_output = open(FILE_PATH_OUTPUT, 'a')
        for item in data:
            file_output.write(item[0])
            i += item[1]
        print("{} 条数据被加入！".format(i))
