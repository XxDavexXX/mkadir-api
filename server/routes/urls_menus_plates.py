from django.urls import path
from server.views.views_menu_plate import getMenusPlates

urlpatterns = [
    path('',getMenusPlates.as_view(),name="get_menus_plates")
]
