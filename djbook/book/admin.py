from django.contrib import admin
from .models import Dbbook


@admin.register(Dbbook)
class dbbookadmin(admin.ModelAdmin):
    list_display = ('id', 'bookname', 'yjhpj', 'author')
    ordering = ('id', )
