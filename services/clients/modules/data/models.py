from django.db import models
from django.db.models.fields.files import ImageField
class Client(models.Model):

    cpf = models.CharField(max_length=12, primary_key=True, null=False, blank=False)
    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256, null=True, blank=True)

    birthdate = models.DateField(null=True, blank=True)

class ClientDetails(models.Model):

    social_name = models.CharField(max_length=512, null=True, blank=True)
    mother_name = models.CharField(max_length=512, null=True, blank=True)
    father_name = models.CharField(max_length=512, null=True, blank=True)
    photo = models.ImageField(default='default.jpg', upload_to='profile_image')

    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='details')

class Address(models.Model):

    city = models.CharField(max_length=256, null=True, blank=True)
    street = models.CharField(max_length=256, null=True, blank=True)
    country = models.CharField(max_length=256, null=True, blank=True)
    state = models.CharField(max_length=256, null=True, blank=True)
    district = models.CharField(max_length=256, null=True, blank=True)
    zip_code = models.CharField(max_length=32, null=True, blank=True)
    
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='address')
