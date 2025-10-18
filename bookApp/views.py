from django.shortcuts import render
from rest_framework import generics
from drf_spectacular.utils import extend_schema
from .models import *
from .serializers import *


# Create your views here.

@extend_schema(tags=["Books"])
class BooksList(generics.ListCreateAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BooksSerializer


@extend_schema(tags=["Books"])
class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BooksSerializer


@extend_schema(tags=["Authors"])
class AuthorsList(generics.ListCreateAPIView):
    queryset = AuthorsModel.objects.all()
    serializer_class = AuthorsSerializer


@extend_schema(tags=["Authors"])
class AuthorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorsModel.objects.all()
    serializer_class = AuthorsSerializer

@extend_schema(tags=["BorrowRecords"])
class BorrowRecordsList(generics.ListCreateAPIView):
    queryset = BorrowRecordsModel.objects.all()
    serializer_class = BorrowRecordsSerializer

@extend_schema(tags=["BorrowRecords"])
class BorrowRecordDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = BorrowRecordsModel.objects.all()
    serializer_class = BorrowRecordsSerializer