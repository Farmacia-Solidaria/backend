from django.contrib import admin
from django.urls import path

from .views import ProductViewset

urlpatterns = [
    path('products/<slug:action>', ProductViewset.as_view()),
]
