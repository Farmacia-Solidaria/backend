from django.db import models
class Role(models.Model):
    name = models.CharField("name", max_length=64, primary_key=True)
    description = models.CharField(max_length=256)
    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.name