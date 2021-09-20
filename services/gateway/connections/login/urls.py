from django.contrib import admin
from django.urls import path

from .views import LoginViewset

urlpatterns = [
    path('login/<slug:action>', LoginViewset.as_view()),
]
