from django.urls import path
from server.views.views_restaurants import getRestaurants
urlpatterns = [
    path('',getRestaurants.as_view())
]
