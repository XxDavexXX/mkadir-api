from django.urls import path 
from server.views.views_plate import getPlates
urlpatterns = [
    path('',getPlates.as_view(),name="get_plates")
]
