from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from .models import Profile

User = get_user_model()


# ----------------------------
# 1. CREATE PROFILE AUTOMATICALLY
# ----------------------------
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)


# ----------------------------
# 2. ASSIGN DEFAULT ROLE
# ----------------------------
@receiver(post_save, sender=User)
def assign_default_role(sender, instance, created, **kwargs):

    if created:
        group, _ = Group.objects.get_or_create(name="customer")
        instance.groups.add(group)