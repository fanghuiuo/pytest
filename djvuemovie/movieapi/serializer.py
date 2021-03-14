from rest_framework import serializers
from .models import Dbmovie, User, Permission, Role


class movieserializer(serializers.ModelSerializer):
    class Meta:
        model = Dbmovie
        fields = '__all__'


class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class Permissionserializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class Roleserializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
