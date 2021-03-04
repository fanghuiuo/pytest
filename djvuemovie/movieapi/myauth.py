from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from .models import UserToken


# 认证类
class Loginauth(BaseAuthentication):
    def authenticate(self, request):
        # 1. 直接在请求头中获取token
        token = request.META.get("HTTP_AUTHORIZATION")
        token_obj = UserToken.objects.filter(token=token).first()

        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        else:
            return (token_obj.username, token_obj)


# 权限管理
class MyPermission(object):
    message = '你没有权限查看'

    def has_permission(self, request, view):
        user_type = request.user.user_type
        if user_type != 2:
            # 返回False表示认证失败
            return False
        else:

            # 返回False表示认证成功
            return True
