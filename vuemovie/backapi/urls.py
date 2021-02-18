from rest_framework.urls import path
from . import views
urlpatterns = [
    path('api/', views.movieviewsets.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/<int:pk>', views.movieviewsets.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('api/getfilter', views.movieviewsets.as_view({'get': 'getfilter'})),
]
