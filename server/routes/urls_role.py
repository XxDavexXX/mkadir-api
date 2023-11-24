from django.urls import path
from server.views.views_role import getRoles
urlpatterns = [
    path('',getRoles.as_view(),name="get_roles")
]
