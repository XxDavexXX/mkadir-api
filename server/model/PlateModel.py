from django.db import models
from server.model.CategoryPlateModel import CategoryPlate
from server.model.RestaurantModel import Restaurant
from server.model.MenuModel import Menu
class Plate(models.Model):
    img_url = models.URLField(max_length=4000)
    name = models.CharField(max_length=255)  
    description = models.TextField()  
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)  
    category = models.ForeignKey(CategoryPlate, on_delete=models.SET_NULL, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name