from django.contrib import admin
from django.urls import path

from .views import UserConnection

urlpatterns = [
    path('users/<slug:action>', UserConnection.as_view()),
]
