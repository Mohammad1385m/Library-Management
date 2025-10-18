from django.urls import path
from .views import *

urlpatterns = [
    path("", UsersList.as_view()),
    path("<pk>/", UserDetails.as_view()),
    path("borrowers/", BorrowersList.as_view()),
    path("borrowrers/<pk>/", BorrowerDetails.as_view())
]