from .views import TestViewset
from django.urls import path

urlpatterns = [
    path("test", TestViewset.as_view())
]
