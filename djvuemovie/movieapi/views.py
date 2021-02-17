from rest_framework import viewsets
from .models import Dbmovie
from .serializer import movieserializer
from rest_framework.response import Response
from .page import fenye
from django.shortcuts import render


class movieviewset(viewsets.ModelViewSet):
    queryset = Dbmovie.objects.all().order_by('id')
    serializer_class = movieserializer
    #pagination_class = fenye  #分页

    def queryfind(self, request):
        tt = Dbmovie.objects.filter(gfwz__contains='www')
        pp = Dbmovie.objects.filter(id__in=[3, 5, 8, 6])
        sl = movieserializer(tt, many=True)
        return Response(sl.data)

    def axios(request):
        return render(request, 'axios.html') # 模板页
