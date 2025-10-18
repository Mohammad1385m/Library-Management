from django.urls import path
from .views import *

urlpatterns = [
    path("books/", BooksList.as_view()),
    path("books/<pk>/", BookDetails.as_view()),
    path("authors/", AuthorsList.as_view()),
    path("authors/<pk>/", AuthorDetails.as_view()),
    path("borrowrecords/", BorrowRecordsList.as_view()),
    path("borrowrecords/<pk>/", BorrowRecordDetails.as_view())
]