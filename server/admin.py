from django.contrib import admin
from .models import User,Restaurant,CategoryPlate,Plate,Menu,MenuPlate,Employee,Role
# Register your models here.
admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(CategoryPlate)
admin.site.register(Plate)
admin.site.register(Menu)
admin.site.register(MenuPlate) #intermediate table
admin.site.register(Role)
admin.site.register(Employee)