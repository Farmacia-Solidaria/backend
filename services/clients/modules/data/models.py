from django.db import models
from cpf_field.models import CPFField
from django.db.models.fields.files import ImageField

class Address(models.Model):

    city = models.CharField(max_length=256, null=True, blank=True)
    street = models.CharField(max_length=256, null=True, blank=True)
    country = models.CharField(max_length=256, null=True, blank=True)
    state = models.CharField(max_length=256, null=True, blank=True)
    district = models.CharField(max_length=256, null=True, blank=True)
    zip_code = models.CharField(max_length=32, null=True, blank=True)

class Client(models.Model):

    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256, null=True, blank=True)
    cpf = CPFField('cpf', primary_key=True)

    birthdate = models.DateField(null=True, blank=True)

    details = models.OneToOneField('ClientDetails', on_delete=models.CASCADE)

class ClientDetails(models.Model):

    social_name = models.CharField(max_length=512, null=True, blank=True)
    mother_name = models.CharField(max_length=512, null=True, blank=True)
    father_name = models.CharField(max_length=512, null=True, blank=True)
    addresses = models.ForeignKey(Address, on_delete=models.CASCADE)
    photo = models.ImageField(default='default.jpg', upload_to='profile_image')
    
