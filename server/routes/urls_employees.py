from django.urls import path
from server.views.views_employees import getEmployees,createEmployee,deleteEmployee,updateEmployee

urlpatterns = [
    path('',getEmployees.as_view(),name="get_employees"),
    path('get/<int:employee_id>/', getEmployees.as_view(), name="get_employees"),
    path('create/',createEmployee.as_view(), name="create_employee"),
    path('delete/<int:employee_id>/', deleteEmployee.as_view(), name="delete_employee"),
    path('update/<int:employee_id>/',updateEmployee.as_view(), name="update_employee"),
]
