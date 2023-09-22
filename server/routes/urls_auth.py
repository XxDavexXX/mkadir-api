from django.urls import path
from server.views.views_auth import RegisterView,LoginWiew,UserView,LogoutView
urlpatterns = [
    path('register',RegisterView.as_view()),
    path('login',LoginWiew.as_view()),
    path('user',UserView.as_view()),
    path('logout',LogoutView.as_view()),
]
