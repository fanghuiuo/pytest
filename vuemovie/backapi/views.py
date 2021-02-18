from .models import Dbmovie
from .serailizers import movieserailizer
from rest_framework.response import Response
from rest_framework import viewsets


class movieviewsets(viewsets.ModelViewSet):
    queryset = Dbmovie.objects.all().order_by('id')
    serializer_class = movieserailizer

    def getfiter(self, request):
        ft = Dbmovie.objects.filter(gfwz__contains='www')
        ftsl = movieserailizer(ft, many=True)
        return Response(ftsl.data)
