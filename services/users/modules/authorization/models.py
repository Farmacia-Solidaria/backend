from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    
    users = models.ManyToManyField(User)
    name = models.CharField("name", max_length=64, primary_key=True)

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.name