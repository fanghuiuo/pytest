from django.urls import path
from . import views
urlpatterns = [
    path('movie/', views.movieviewset.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('movie/<int:pk>', views.movieviewset.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('test/', views.movieviewset.as_view({'get': 'test'})),
]
