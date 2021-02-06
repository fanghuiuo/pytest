from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import blog
# Create your views here.


def index(request):
    return HttpResponse('hello world')


def getxx(request, blogid):
    xx = get_object_or_404(blog, pk=blogid)
    context = {}
    context['xx'] = xx
    return render(request, 'index.html', context)
    # return HttpResponse('标题: %s <br> 内容：%s' % (xx.title, xx.content))
