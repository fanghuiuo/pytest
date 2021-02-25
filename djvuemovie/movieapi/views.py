from rest_framework import viewsets
from .models import Dbmovie
from .serializer import movieserializer
# from rest_framework.response import Response
# from .page import fenye
# from django.shortcuts import render
# from django.db.models import Q
from .filter import moviefilter


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
    filter_class = moviefilter

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
