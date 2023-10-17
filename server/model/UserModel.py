from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    paternal_surname = models.CharField(max_length=255)
    maternal_surname = models.CharField(max_length=255)
    dni = models.CharField(max_length=30)
    picture = models.URLField(max_length=2000, default=None, blank=True, null=True)
    username = models.CharField(max_length=255, unique=True)
    
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['password','name','paternal_surname','maternal_surname','dni','username']