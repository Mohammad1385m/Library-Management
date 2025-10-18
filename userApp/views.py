from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics
from drf_spectacular.utils import extend_schema
from .models import *
from .serializers import *

# Create your views here.

User = get_user_model()


@extend_schema(tags=["Users"])
class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


@extend_schema(tags=["Users"])
class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


@extend_schema(tags=["Borrowers"])
class BorrowersList(generics.ListCreateAPIView):
    queryset = BorrowersModel.objects.all()
    serializer_class = BorrowersSerializer


@extend_schema(tags=["Borrowers"])
class BorrowerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = BorrowersModel.objects.all()
    serializer_class = BorrowersSerializer
