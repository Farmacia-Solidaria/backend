from django.contrib import admin
from django.urls import path

from .views import UsersConnection

urlpatterns = [
    path('users/<slug:action>', UsersConnection.as_view()),
]
