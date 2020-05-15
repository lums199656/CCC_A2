import json
import certifi
import ssl
import geopy.geocoders
from geopy.geocoders import Nominatim
from textblob import TextBlob


def coo_to_city(coordinates):  # coordinates = "-36.97935827, 145.05330569"
    locator = Nominatim(user_agent="ccc_geo")
    location = locator.reverse(coordinates)
    location = str(location).split(", ")

    for loc in location:
        if loc.isdigit():
            location.remove(loc)
    location = location[-3].split(' ')[-1].upper()
    return location


if __name__ == '__main__':
    ctx = ssl.create_default_context(cafile=certifi.where())
    geopy.geocoders.options.default_ssl_context = ctx
    FILE_PATH_IMPORT = '/Users/luminshen/Desktop/CCC/twitter-melb.json'
    FILE_PATH_OUTPUT = '/Users/luminshen/Desktop/CCC/twitter-melb-location.json'
    LOG_PATH = '/Users/luminshen/Desktop/CCC/log.txt'

    file_output = open(FILE_PATH_OUTPUT, 'a')
    file_log = open(LOG_PATH, 'a')
    month = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
             'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

    with open(FILE_PATH_IMPORT) as file:
        index_ = 0
        total_row = 0
        datagram = []
        while True:
            line = file.readline().rstrip(',\n')
            if index_ == 0:
                total_row = int(line[14:23])
                index_ += 1
                print('0 %')
                continue
            if line == ']}':
                break
            else:
                doc = json.loads(line)
                if ('doc' not in doc) or (len(doc['doc']['entities']['hashtags']) == 0):
                    continue

                # 将坐标转化成城市👇
                coordinate = str(list(reversed(doc['doc']['coordinates']['coordinates'])))[1:-1]
                try:
                    doc['doc']['location'] = coo_to_city(coordinate)
                except:
                    print(str(index_) + " error\n")
                    file_log.write(str(index_) + " error\n")
                    continue
                # 将坐标转化成城市👆

                # 处理情感👇 sentiments_exact: 储存具体数值; sentiments_booleant: 储存-1,0,1
                blob = TextBlob(doc['doc']['text'])
                sentiment = blob.sentiment[0]
                doc['doc']['sentiments_exact'] = sentiment
                if sentiment > 0:
                    sentiment = 1
                elif sentiment < 0:
                    sentiment = -1
                else:
                    sentiment = int(sentiment)
                doc['doc']['sentiments_boolean'] = sentiment
                # 处理情感👆

                # 处理 hashtags👇
                hashtags = doc['doc']['entities']['hashtags']
                doc['doc']['hashtags'] = []
                for hashtag in hashtags:
                    doc['doc']['hashtags'].append(hashtag['text'].lower())
                # 处理 hashtags👆

                # 处理 时间👇
                time = doc['doc']['created_at'].split(" ")
                time = int(time[-1] + month[time[1]] + time[2])
                doc['doc']['timestamp'] = time
                # 处理 时间👆
                print(doc['doc']['location'], '|', doc['doc']['sentiments_exact'], doc['doc']['sentiments_boolean'],
                      '|', doc['doc']['hashtags'], '|',
                      doc['doc']['timestamp'])
                file_output.write(str(doc) + '\n')
                index_ += 1
            if index_ % 100000 == 0:
                print(str(index_ / total_row * 100), "%")
        print('处理完成', str(index_), '条数据')
