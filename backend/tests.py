import json

from django.test import TestCase


# Create your tests here.
# 提取 vic_geo.json 的城市
# with open('/Users/luminshen/Desktop/output.txt', 'a') as output:
#     with open('/Users/luminshen/Desktop/vic_geo.json') as file:
#         file_ = json.load(file)['features']
#         for line in file_:
#             ct_name = line['properties']['vic_loca_2']
#             print(ct_name)
#             output.write(ct_name + ",")

#


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


output = open('/Users/luminshen/Desktop/CCC/twitter.json', 'a')
file_location = open('/Users/luminshen/Desktop/CCC/twitter-melb-location.json')
file = open('/Users/luminshen/Documents/代码/PycharmProjects/A2_/couchdb/vic_geo.json')
file = json.load(file)['features']

i = 0
set_ = set()
for index_, line_ in enumerate(file_location):
    line_ = eval(line_)
    [x, y] = line_['doc']['coordinates']['coordinates']
    for line in file:
        # x = 10
        # y = 1
        polygon = line['geometry']['coordinates'][0]
        # polygon = [[0.0, 0.0], [20.0, 0.0], [0.0, 20.0], [20.0, 20.0]]
        if IsPtInPoly(x, y, polygon):
            # print(line['properties']['vic_loca_2'])
            line_['doc']['location'] = line['properties']['vic_loca_2']
            set_.add(line['properties']['vic_loca_2'])
            output.write(str(line_)+"\n")
            i += 1
    if index_ % 1000 == 0:
        print("已经处理了 {} 条".format(index_))
print("{} 条数据被加入！".format(i))
print("{} 个 suburbs 的数据被新增".format(len(set_)))
