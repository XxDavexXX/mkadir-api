from django.db import models
from .UserModel import User
class Restaurant(models.Model):
    logo_url = models.URLField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['name','address','user']
    
    def __str__(self):
        return  self.name
