from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
import couchdb
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/spider/')
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


def get_sentiments(request):
    USER = 'admin'
    PASSWORD = 'admin'
    couchDB = couchdb.Server("http://{}:{}@115.146.95.221:5984/".format(USER, PASSWORD))
    dbname = "twitter_crawl"
    db = couchDB[dbname]
    db_sentiments = db.view("suburbs/sentiments", group=True, group_level=3)
    db_hashtags = db.view("suburbs/hashtags", group=True, group_level=3)
    ret = {}
    for item in db_sentiments:
        print(item.key, item.value)
        if ret.get(item.key[0]) is None:
            ret[item.key[0]] = {1: 0, 0: 0, -1: 0, 'sum': 0, '1_percent': 0.0, '0_percent': 0.0, '-1_percent': 0.0,
                                '1_hastags': [], '0_hastags': [], '-1_hastags': [], '1_hastags_num': [],
                                '0_hastags_num': [], '-1_hastags_num': []}
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
    print('---------------------------')
    for item in db_hashtags:
        if item.key is None:
            continue
        print(item.key, item.value)
        set_ = set()  # 定义集合
        num_ = []
        for v in item.value:  # 循环列表中的元素
            if v not in set_:  # 如果i不在集合中
                set_.add(v)  # 将i添加到集合中
                num_.append(item.value.count(v))
        sort_ = zip(num_, list(set_))
        sort_ = sorted(sort_, reverse=True)
        num_, set_ = zip(*sort_)
        if item.key[1] == -1:
            ret[item.key[0]]['-1_hastags'] = set_
            ret[item.key[0]]['-1_hastags_num'] = num_
        elif item.key[1] == 1:
            ret[item.key[0]]['1_hastags'] = set_
            ret[item.key[0]]['1_hastags_num'] = num_
        elif item.key[1] == 0:
            ret[item.key[0]]['0_hastags'] = set_
            ret[item.key[0]]['0_hastags_num'] = num_

    return HttpResponse(json.dumps(ret))


def crawl(request):
    pass
