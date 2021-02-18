from rest_framework import serializers
from .models import Dbmovie


class movieserailizer(serializers.ModelSerializer):
    class Meta:
        model = Dbmovie
        fields = '__all__'
