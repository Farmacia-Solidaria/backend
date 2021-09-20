from django.contrib import admin
from django.urls import path

from .views import UserViewset

urlpatterns = [
    path('users/<slug:action>', UserViewset.as_view()),
]
