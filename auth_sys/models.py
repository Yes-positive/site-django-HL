from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    ROLES_CHOICES = [
        ('moder', 'Moder'),
        ('user', 'User'),
        ('admin', 'Admin'),
    ]

    roles = models.CharField(max_length=10, choices=ROLES_CHOICES, default='user')

