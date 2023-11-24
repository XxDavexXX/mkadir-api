from django.urls import path,include
from server.views.views_restaurants import createRestaurant,getAllRestaurants,getRestaurants,registerRestaurant,getRestaurant,deleteRestaurant,updateRestaurant
from server.views.views_employees import EmployeeDetailView

urlpatterns = [
    path('all',getAllRestaurants.as_view()),
    path('',getRestaurants.as_view()),
    path('create',createRestaurant.as_view()),
    path('register',registerRestaurant.as_view()),
    path('<int:restaurant_id>',getRestaurant.as_view()),
    path('delete/<int:restaurant_id>',deleteRestaurant.as_view()),
    path('update/<int:restaurant_id>',updateRestaurant.as_view()),
    path('<int:restaurant_id>/employees/<int:employee_id>/', EmployeeDetailView.as_view(), name="employee_detail"),

    # Plates
    path('plates/<int:restaurant_id>/',include('server.routes.urls_plates')),
    # Employees
    path('<int:restaurant_id>/employees/',include('server.routes.urls_employees')),
    # EmployeesProfiles
    path('<int:restaurant_id>/employees/<int:employee_id>/',include('server.routes.urls_employees')),

    #Menus
    path('<int:restaurant_id>/menus/',include('server.routes.urls_menus')),
    # Roles
    path('roles/',include('server.routes.urls_role')),
    
]
