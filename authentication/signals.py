from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import UserProfile


User = get_user_model()


@receiver(post_save, sender=User)
def create_profile_for_user(sender, instance=None, created=False, **kwargs):
    if created and instance:
        UserProfile.objects.get_or_create(user=instance)


@receiver(pre_delete, sender=User)
def delete_prfile_for_user(sender, instance=None, **kwargs):
    if instance:
        try:
            user_profile = UserProfile.objects.get(user=instance)
        except UserProfile.DoesNotExist:
            pass
        else:
            user_profile.delete()
