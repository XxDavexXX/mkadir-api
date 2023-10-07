from django.db import models
from django.utils import timezone
from server.model.RestaurantModel import Restaurant
class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " Is Published " + str(self.is_published)
