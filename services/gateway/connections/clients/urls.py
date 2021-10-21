from django.contrib import admin
from django.urls import path

from .views import ClientsConnection

urlpatterns = [
    path('clients/<slug:action>', ClientsConnection.as_view()),
]
