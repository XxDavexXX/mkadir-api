from django.urls import path
from server.views.views_api import IndexApiView
urlpatterns = [
    path('',IndexApiView.as_view(),name='index_api_view')
]
