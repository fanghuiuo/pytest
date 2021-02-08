from rest_framework.decorators import api_view
from rest_framework import status
from .models import Dbbook
from .serializers import bookserializers
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def getpost(request, pk):
    if request.method == 'GET':
        bookset = Dbbook.objects.all()
        serializer = bookserializers(instance=bookset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = bookserializers(data=request.data)
        # 数据验证
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
