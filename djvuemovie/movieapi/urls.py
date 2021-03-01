from django.urls import path
from .views import movieviewset, userviewset, LoginView
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])
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
    path('docs/', schema_view),
    path('api/login', userviewset.as_view({
        'get': 'list',
    })),
    path('login/', LoginView.as_view()),
    # path('api/queryfind', movieviewset.as_view({'get': 'queryfind'})),
    # path('', movieviewset.axios),  # 模板页
]
