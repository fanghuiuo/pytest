from django.shortcuts import render
from .models import Dbmovie


def getlist(request):
    books = Dbmovie.objects.all()
    return render(request, 'list.html', {'books': books})
