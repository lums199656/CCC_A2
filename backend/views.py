from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
import couchdb
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/spider/')
import savetweets
import TweetStore


def go_to_map(request):
    return render(request, 'map.html')


def go_to_chart(request):
    return render(request, 'chart.html')


def go_to_home(request):
    return render(request, 'home.html')


def get_aurin(request):
    return HttpResponse(json.dumps({'a': 1}))


def spider(request):
    savetweets.start()
    return HttpResponse('DONE!')


def transfer_suburb(raw):
    pass


def get_hashtags(request):
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

def get_sentiments(request):
    USER = 'admin'
    PASSWORD = 'admin'
    couchDB = couchdb.Server("http://{}:{}@115.146.95.221:5984/".format(USER, PASSWORD))
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
