from django.urls import path

from server.views.views_menus import getMenus,getMenuIsPublished

urlpatterns = [
    path('',getMenus.as_view(),name="get_menus"),
    path('is-published',getMenuIsPublished.as_view(),name="get_menus_is_published")
]
