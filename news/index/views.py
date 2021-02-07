from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import news


def index(request):
    return HttpResponse('哈哈哈哈哈哈')


def getxx(request, newsid):
    xx = get_object_or_404(news, pk=newsid)
    return render(request, 'xx.html', {'xx': xx})


def getlist(request):
    newslist = news.objects.all()
    return render(request, 'newslist.html', {'newslist': newslist})
