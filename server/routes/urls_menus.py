from django.urls import path

from server.views.views_menus import getMenus,getMenuIsPublished,getMenu,createMenu,updateMenu,deleteMenu,getMenusIsPublished

urlpatterns = [
    path('',getMenus.as_view(),name="get_menus"),
    path('create',createMenu.as_view(),name="create_menu"),
    path('update/<int:menu_id>',updateMenu.as_view(),name="update_menu"),
    path('delete/<int:menu_id>',deleteMenu.as_view(),name="delete_menu"),
    path('<int:menu_id>',getMenu.as_view(),name="get_menu"),
    path('is-published',getMenuIsPublished.as_view(),name="get_menus_is_published"),
    path('is-publisheds',getMenusIsPublished.as_view(),name="get_menus_is_published")
]
