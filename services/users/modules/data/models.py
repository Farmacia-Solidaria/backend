from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ManyToManyField

from modules.authorization.models import Role

class City(models.Model):
    name = models.CharField(max_length=256)
    state = models.CharField(max_length=2)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ManyToManyField('City', blank=True)
    role = models.ManyToManyField(Role, blank=True)