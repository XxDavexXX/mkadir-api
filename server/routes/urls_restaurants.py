from django.urls import path
from server.views.views_restaurants import RegisterWiew
urlpatterns = [
    path('',RegisterWiew)
]
