from django.contrib import admin
from .models import Dbmovie


@admin.register(Dbmovie)
class dbmovieadmin(admin.ModelAdmin):
    list_display = ('id', 'dym', 'ym')
    ordering = ('id', )
