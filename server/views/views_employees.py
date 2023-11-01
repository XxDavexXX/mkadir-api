from rest_framework.views import APIView
from rest_framework.response import Response
from server.model.EmployeeModel import Employee
from server.model.RoleModel import Role
from server.model.UserModel import User
from server.serializers.EmployeeSerializer import EmployeeSerializer
from server.middlewares.AuthMiddleware import AuthRequired
from rest_framework.exceptions import AuthenticationFailed
from django.shortcuts import get_object_or_404
from server.model.RestaurantModel import Restaurant

class getEmployees(APIView):
    def get(self, request, restaurant_id):
        employees = Employee.objects.filter(restaurant_id=restaurant_id)
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data)        

class EmployeeDetailView(APIView):
    def get(self, request, restaurant_id, employee_id):
        try:
            employee = Employee.objects.get(restaurant_id=restaurant_id, id=employee_id)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response("Employee not found", status=404)       
        
class createEmployee(APIView):
    def post(self, request, restaurant_id):
        user_id = request.data.get('user')
        role_id = request.data.get('role')
        dni = request.data.get('dni')
        address = request.data.get('address')
        age = request.data.get('age')
        phone = request.data.get('phone')

        if not (user_id and role_id):
            return Response({'message': 'User, Role, and DNI are required fields'}, status=400)

        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=404)

        try:
            role = Role.objects.get(id=role_id)
        except Role.DoesNotExist:
            return Response({'message': 'Role not found'}, status=404)

        # Crea un nuevo empleado con los datos proporcionados
        employee = Employee(
            user=user, restaurant=restaurant, role=role, dni=dni,
            address=address, age=age, phone=phone
        )
        employee.save()
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=201)

class deleteEmployee(APIView):
    def delete(self, request, restaurant_id, employee_id):
        try:
            employee = Employee.objects.get(id=employee_id)
            employee.delete()
            return Response({'message': 'Employee deleted successfully'}, status=200)
        except Employee.DoesNotExist:
            return Response({'message': 'Employee not found'}, status=404)

class updateEmployee(APIView):
    def put(self, request, restaurant_id, employee_id):
        try:
            employee = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            return Response({'message': 'Employee not found'}, status=404)
  
        new_role_id = request.data.get('role')
        new_user_id = request.data.get('user')
        
        if new_role_id is not None:
            try:
                new_role = Role.objects.get(id=new_role_id)
                employee.role = new_role
            except Role.DoesNotExist:
                return Response({'message': 'New role not found'}, status=404)
        
        if new_user_id is not None:
            try:
                new_user = User.objects.get(id=new_user_id)
                employee.user = new_user
            except User.DoesNotExist:
                return Response({'message': 'New user not found'}, status=404)
            
         # Actualizar otros campos propios de Employee
        if 'address' in request.data:
            employee.address = request.data['address']
        if 'age' in request.data:
            employee.age = request.data['age']
        if 'dni' in request.data:
            employee.dni = request.data['dni']
        if 'phone' in request.data:
            employee.phone = request.data['phone']

        employee.save()
        return Response({'message': 'Employee updated successfully'}, status=200)
