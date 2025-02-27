from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TheUser, Profile

@receiver(post_save, sender=TheUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=TheUser)
def save_profile(sender, instance, **kwargs):
    instance.Profile.save()