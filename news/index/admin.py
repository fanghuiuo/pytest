from django.contrib import admin
from .models import news


@admin.register(news)
class newsadmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'addtime', 'changetime', 'is_del')
    ordering = ('id', )
