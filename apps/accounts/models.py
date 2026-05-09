
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email=models.EmailField(unique=True)
    
    def __str__(self):
        return self.username


from apps.accounts.validators import phone_validator,national_id_validator,name_validator

class Customer(models.Model):
    name= models.CharField(max_length=150, validators=[name_validator])
    phone = models.CharField(max_length=13, validators=[phone_validator])
    national_id = models.CharField(max_length=10, validators=[national_id_validator]) 
