from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    #path('newslist/', views.getlist),
    #path('newslist/<int:newsid>', views.getxx),
]
