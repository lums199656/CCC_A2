from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
import couchdb

API_KEY = 'de9dECvvcd48CfEdvfDrgbtD'


def go_to_map(request):
    return render(request, 'map.html')


def go_to_chart(request):
    return render(request, 'chart.html')


def go_to_home(request):
    return render(request, 'home.html')


def get_aurin(request):
    return HttpResponse(json.dumps({'a': 1}))


def transfer_suburb(request):
    pass


def get_hashtags(request):
    global API_KEY
    api_key = request.headers.get("X-API-KEY")
    if api_key != API_KEY:
        return HttpResponse("Unauthorized")
    USER = 'admin'
    PASSWORD = 'admin'
    couchDB = couchdb.Server("http://{}:{}@115.146.95.221:5984/".format(USER, PASSWORD))
    # dbname = "twitter_crawl"
    dbname = "twitter_crawl"
    db = couchDB[dbname]
    db_hashtags = db.view("Test2/Test2", group=True, group_level=3)
    ret = {}
    for item in db_hashtags:
        location = item.key[0]
        sentiment = item.key[1]
        data = item.value
        print(item.key, item.value)
        if ret.get(location) is None:
            ret[location] = {'1_hastags': [], '0_hastags': [], '-1_hastags': [], '1_hastags_num': 0,
                             '0_hastags_num': 0, '-1_hastags_num': 0}
        if sentiment == -1:
            ret[location]['-1_hastags'] = data['hashtags']
            ret[location]['-1_hastags_num'] = data['sum']
        elif sentiment == 1:
            ret[location]['1_hastags'] = data['hashtags']
            ret[location]['1_hastags_num'] = data['sum']
        elif sentiment == 0:
            ret[location]['0_hastags'] = data['hashtags']
            ret[location]['0_hastags_num'] = data['sum']

    return HttpResponse(json.dumps(ret))


def get_sentiments_avg(request):
    pass


def upload_to_couchdb(request):
    IP_ADDRESS = '45.113.234.69'
    # DB_NAME = 'demo_2'
    DB_NAME = 'twitter-2018'
    FILE_PATH = '/Users/luminshen/Desktop/CCC/twitter-data/twitter-2018-processed.json'

    couch = couchdb.Server('http://admin:admin@{}:5984/'.format(IP_ADDRESS))
    try:
        db = couch.create(DB_NAME)
    except couchdb.http.PreconditionFailed:
        print(DB_NAME, '已存在')

    db = couch[DB_NAME]
    with open(FILE_PATH) as file:
        index_ = 0
        datagram = []
        while True:
            try:
                line = file.readline().rstrip(',\n')
                if len(line) < 10:
                    print('处理结束！')
                    break
                if index_ == 0:
                    print('开始处理...')
                else:
                    line = eval(line)['doc']
                    datagram.append(line)
                    if index_ % 1000 == 0:
                        db.update(datagram)
                        datagram = []
                if index_ % 1000 == 0:
                    print('已经处理了 {} 条'.format(index_))
            except:
                print(index_, ' error')
                print(line)
            index_ += 1
    return HttpResponse('UPLOAD DONE!')


def get_sentiments(request):
    global API_KEY
    api_key = request.META.get("X-API-KEY")
    if api_key != API_KEY:
        return HttpResponse("Unauthorised")

    USER = 'admin'
    PASSWORD = 'admin'
    couchDB = couchdb.Server("http://{}:{}@45.113.234.69:5984/".format(USER, PASSWORD))
    # dbname = "twitter_crawl"
    dbname = "demo"
    db = couchDB[dbname]
    db_sentiments = db.view("suburbs/sentiments", group=True, group_level=3)
    ret = {}
    for item in db_sentiments:
        if ret.get(item.key[0]) is None:
            ret[item.key[0]] = {1: 0, 0: 0, -1: 0, 'sum': 0, '1_percent': 0.0, '0_percent': 0.0, '-1_percent': 0.0}
            ret[item.key[0]][item.key[1]] = item.value
            ret[item.key[0]]['sum'] += item.value
        else:
            ret[item.key[0]][item.key[1]] = item.value
            ret[item.key[0]]['sum'] += item.value

        if item.key[1] == 1:
            if ret[item.key[0]][1] != 0:
                ret[item.key[0]]['1_percent'] = float(ret[item.key[0]][1]) / float(ret[item.key[0]]['sum'])
            if ret[item.key[0]][0] != 0:
                ret[item.key[0]]['0_percent'] = float(ret[item.key[0]][0]) / float(ret[item.key[0]]['sum'])
            if ret[item.key[0]][-1] != 0:
                ret[item.key[0]]['-1_percent'] = float(ret[item.key[0]][-1]) / float(ret[item.key[0]]['sum'])
    return HttpResponse(json.dumps(ret))


def crawl(request):
    pass
