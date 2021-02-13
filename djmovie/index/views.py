from rest_framework import viewsets
from .models import Dbmovie
from .serializers import movieserializer
from .pagination import fenye
from rest_framework.response import Response


class movieviewset(viewsets.ModelViewSet):
    queryset = Dbmovie.objects.all().order_by('id')
    serializer_class = movieserializer
    pagination_class = fenye

    def test(self, request):
        www = Dbmovie.objects.filter(gfwz__contains='www')
        tt = Dbmovie.objects.filter(id__in=[1, 5, 7, 9])
        eee = Dbmovie.objects.exclude(id=3)
        ss = movieserializer(www, many=True)
        return Response(ss.data)
