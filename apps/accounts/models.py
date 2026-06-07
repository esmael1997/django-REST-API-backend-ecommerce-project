from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.accounts.validators import (
    phone_validator,
    national_id_validator,
    name_validator,
)


class User(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    def is_customer(self):
        return self.groups.filter(name="customer").exists()

    def is_admin_user(self):
        return (
            self.is_staff or
            self.is_superuser or
            self.groups.filter(name="admin").exists()
        )


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    full_name = models.CharField(
        max_length=150,
        validators=[name_validator],
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=13,
        validators=[phone_validator]
    )

    national_id = models.CharField(
        max_length=10,
        validators=[national_id_validator]
    )

    bio = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.full_name