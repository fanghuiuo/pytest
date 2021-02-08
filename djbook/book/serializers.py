from django.db import models
from rest_framework import serializers
from .models import Dbbook


class bookserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dbbook
        fields = ['id', 'bookname', 'yjhpj']
