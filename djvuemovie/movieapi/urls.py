from django.urls import path
from .views import movieviewset
urlpatterns = [
    path('api/', movieviewset.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/<int:pk>', movieviewset.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('api/queryfind', movieviewset.as_view({'get': 'queryfind'})),
    path('', movieviewset.axios),  # 模板页
]
