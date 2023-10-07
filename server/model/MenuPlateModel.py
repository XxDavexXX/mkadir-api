from django.db import models
from server.model.PlateModel import Plate
from server.model.MenuModel import Menu
from server.model.RestaurantModel import Restaurant 

class MenuPlate(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    plate = models.ForeignKey(Plate, on_delete=models.SET_NULL, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.menu.name

    class Meta:
        unique_together = ('menu', 'plate','restaurant')  # Asegura que no haya duplicados de la relación
