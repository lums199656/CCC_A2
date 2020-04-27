from django.shortcuts import render


def index(request):
    print("在 index 中")
    return render(request, 'main.html')
