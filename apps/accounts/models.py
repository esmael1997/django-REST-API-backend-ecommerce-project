from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.accounts.validators import (
    phone_validator,
    national_id_validator,
    name_validator,
)


class User(AbstractUser):
    email=models.EmailField(unique=True)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.username


class CustomerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='customer_profile'
    )
    
    full_name = models.CharField(
        max_length=150,
        validators=[name_validator]
    )
    
    phone = models.CharField(
        max_length=13,
        validators=[phone_validator]
    )
    
    national_id = models.CharField(
        max_length=10,
        validators=[national_id_validator]
    )
    
    class Meta:
        verbose_name = 'Customer Profile'
        verbose_name_plural = 'Customer Profiles'
        
    def __str__(self):
        return self.full_name
    
class Profile(models.Model):
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    
    bio = models.TextField(
        blank=True,
        null=True
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    def __str__(self):
        return self.user.username
    
