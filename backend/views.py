from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json


def index(request):
    print("在 index 中")
    return render(request, 'main.html')


def get_aurin(request):
    return HttpResponse(json.dumps({'a': 1}))
