from django.urls import path,include
from server.views.views_restaurants import createRestaurant,getAllRestaurants,getRestaurants,registerRestaurant,getRestaurant,deleteRestaurant,updateRestaurant
urlpatterns = [
    path('pages',getAllRestaurants.as_view()),
    path('',getRestaurants.as_view()),
    path('create',createRestaurant.as_view()),
    path('register',registerRestaurant.as_view()),
    path('<int:restaurant_id>',getRestaurant.as_view()),
    path('delete/<int:restaurant_id>',deleteRestaurant.as_view()),
    path('update/<int:restaurant_id>',updateRestaurant.as_view()),
    # Plates
    path('plates/<int:restaurant_id>/',include('server.routes.urls_plates')),

    #Menus
    path('<int:restaurant_id>/menus/',include('server.routes.urls_menus')),
]
