from rest_framework import serializers
from .models import Dbmovie, User


class movieserializer(serializers.ModelSerializer):
    class Meta:
        model = Dbmovie
        fields = '__all__'


class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
