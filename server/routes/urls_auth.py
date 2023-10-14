from django.urls import path
from server.views.views_auth import RegisterView,LoginWiew,UserView,LogoutView
urlpatterns = [
    path('register',RegisterView.as_view(),name='register'),
    path('login',LoginWiew.as_view(),name='login'),
    path('user',UserView.as_view(),name='user'),
    path('logout',LogoutView.as_view()),
]
