from rest_framework import serializers
from .models import *

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = '__all__'

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorsModel
        fields = '__all__'

class BorrowRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecordsModel
        fields = '__all__'