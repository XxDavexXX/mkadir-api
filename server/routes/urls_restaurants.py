from django.urls import path,include
from server.views.views_restaurants import getRestaurants,registerRestaurant
urlpatterns = [
    path('',getRestaurants.as_view()),
    path('register',registerRestaurant.as_view()),

    # Plates
    path('plates/<int:restaurant_id>/',include('server.routes.urls_plates')),

    #Menus
    path('<int:restaurant_id>/menus/',include('server.routes.urls_menus')),
]
