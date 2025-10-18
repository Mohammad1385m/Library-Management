from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *

User = get_user_model()


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BorrowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowersModel
        fields = '__all__'
