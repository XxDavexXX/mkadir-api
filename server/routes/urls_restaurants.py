from django.urls import path
from server.views.views_restaurants import getRestaurants,registerRestaurant
urlpatterns = [
    path('',getRestaurants.as_view()),
    path('register',registerRestaurant.as_view())
]
