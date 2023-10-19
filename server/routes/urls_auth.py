from django.urls import path
from server.views.views_auth import RegisterView,LoginWiew,UserView,LogoutView,VerifyPassword
urlpatterns = [
    path('register',RegisterView.as_view(),name='register'),
    path('login',LoginWiew.as_view(),name='login'),
    path('user',UserView.as_view(),name='user'),
    path('verify_password',VerifyPassword.as_view(),name='verify_password'),
    path('logout',LogoutView.as_view()),
]
