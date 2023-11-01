from django.db import models
from django.utils import timezone
from server.model.RestaurantModel import Restaurant
from server.model.UserModel import User
from server.model.RoleModel import Role

class Employee(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role,on_delete=models.SET_NULL, null=True)
    dni = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    phone = models.CharField(max_length=9)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name
