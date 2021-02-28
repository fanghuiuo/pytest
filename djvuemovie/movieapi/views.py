from rest_framework import viewsets
from .models import Dbmovie, User, UserToken
from .serializer import movieserializer, userserializer
# from rest_framework.response import Response
# from .page import fenye
# from django.shortcuts import render
# from django.db.models import Q
from .filter import moviefilter, userfilter
import hashlib
from rest_framework.views import APIView
import time
from rest_framework.response import Response


class movieviewset(viewsets.ModelViewSet):
    """
    retrieve:
        返回查询结果

    list:
        根据查询条件 返回查询结果 不加参数默认返回所有

    create:
        新建电影记录

    delete:
        删除电影记录

    update:
        更新修改电影记录
    """

    queryset = Dbmovie.objects.all().order_by('id')
    serializer_class = movieserializer
    # 过滤类
    filter_class = moviefilter
    # 指定认证类
    # authentication_classes = [TokenAuthentication, ]

    # pagination_class = fenye  #分页
    '''

    def queryfind(self, request):
        tt = Dbmovie.objects.filter(gfwz__contains='www')
        # pp = Dbmovie.objects.filter(id__in=[3, 5, 8, 6])
        sl = movieserializer(tt, many=True)
        return Response(sl.data)

    def axios(self, request):
        return render(request, 'axios.html')  # 模板页
   '''


class userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = userserializer
    filter_class = userfilter


class LoginView(APIView):
    authentication_classes = []  # 登录验证登陆页面免认证，其余的已经全局配置
    permission_calsses = []  # 权限登陆页面免认证，其余的已经全局配置

    def post(self, request, *args, **kwargs):
        try:
            username = request.data["username"]
            password = request.data["password"]
            user_obj = User.objects.filter(username=username, password=password).first()
            if user_obj:
                # 为登录用户创建token
                token = self.md5(username)
                '''
                # 保存(存在就更新不存在就创建，并设置过期时间为5分钟)
                 expiration_time = datetime.now() + dateutil.relativedelta.relativedelta(minutes=5)
                 print(expiration_time, type(expiration_time))
                defaults = {
                    "token": token,
                    "expiration_time": expiration_time
                }
                '''
                UserToken.objects.update_or_create(user=user_obj, defaults={'token': token})
                return Response({"code": 200, "token": token})
            else:
                return Response({"code": 401, "error": "用户名或密码错误"})
        except Exception as e:
            print(e)
            return Response({"code": 500, "error": "用户名或密码错误"})
    # 生成token

    def md5(self, username):
        m = hashlib.md5(bytes(username, encoding='utf-8'))
        m.update(bytes(str(time.time()), encoding='utf-8'))
        return m.hexdigest()
