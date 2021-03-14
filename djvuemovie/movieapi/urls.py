from django.urls import path
from .views import movieviewset, userviewset, LoginView, Permissionviewset, Roleviewset
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])
urlpatterns = [
    path('api/movie/', movieviewset.as_view({
        'get': 'list',
        'post': 'create'
    })),
    # 权限list
    path('api/permission/', Permissionviewset.as_view({
        'get': 'list'
    })),
    # 权限tree
    #path('api/permissiontree/', PermissiontreeView.as_view()),
    # 角色
    path('api/role/', Roleviewset.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/role/<int:pk>', Roleviewset.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('api/movie/<int:pk>', movieviewset.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('docs/', schema_view),
    path('api/login', userviewset.as_view({
        'get': 'list',
    })),
    # login
    path('login/', LoginView.as_view()),
    # path('api/queryfind', movieviewset.as_view({'get': 'queryfind'})),
    # path('', movieviewset.axios),  # 模板页
    path('api/user/', userviewset.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/user/<int:pk>', userviewset.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
