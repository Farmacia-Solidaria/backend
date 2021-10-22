from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Client, ClientDetails

@receiver(post_save, sender=Client)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ClientDetails.objects.create(client=instance)

@receiver(post_save, sender=Client)
def save_profile(sender, instance, **kwargs):
    instance.details.save()