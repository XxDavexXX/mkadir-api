from django.urls import path,include
from server.views.views_restaurants import getAllRestaurants,getRestaurants,registerRestaurant,getRestaurant
urlpatterns = [
    path('all',getAllRestaurants.as_view()),
    path('',getRestaurants.as_view()),
    path('register',registerRestaurant.as_view()),
    path('<int:restaurant_id>',getRestaurant.as_view()),

    # Plates
    path('plates/<int:restaurant_id>/',include('server.routes.urls_plates')),

    #Menus
    path('<int:restaurant_id>/menus/',include('server.routes.urls_menus')),
]
