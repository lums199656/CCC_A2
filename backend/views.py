from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json


def go_to_map(request):
    return render(request, 'map.html')


def go_to_chart(request):
    return render(request, 'chart.html')


def go_to_home(request):
    return render(request, 'home.html')


def get_aurin(request):
    return HttpResponse(json.dumps({'a': 1}))


def crawl(request):
    pass
