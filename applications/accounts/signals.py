from django.dispatch import receiver
from .models import User
from django.db.models.signals import post_save
from accounts.managers.services import UserProfileService


@receiver(post_save, sender=User)
def create_mother_ship(sender, instance, created, **kwargs):
    if created:
        UserProfileService.create_user_profile(**kwargs)