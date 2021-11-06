from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Address, Client, ClientDetails

@receiver(post_save, sender=Client)
def create_client_details(sender, instance, created, **kwargs):
    if created:
        try:
            if instance.details: pass
        except:
            ClientDetails.objects.create(client=instance)
            
        try:
            if instance.address: pass
        except:
            Address.objects.create(client=instance)

@receiver(post_save, sender=Client)
def save_client(sender, instance, **kwargs):
    instance.details.save()
    instance.address.save()