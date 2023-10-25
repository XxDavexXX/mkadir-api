from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from server.models import User
from server.serializers.UserSerializer import UserSerializer,LoginSerializer,PasswordSerializer
import jwt,datetime
# # Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # get id an email
        user_id = serializer.instance.id
        user_email = serializer.instance.email

        payload = {
            'id': user_id,
            'name': user_email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        # Generate token JWT
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        # Create cookie
        response = Response()
        expires = datetime.datetime.utcnow() + datetime.timedelta(days=2)
        response.set_cookie(key='jwt', value=token, httponly=True, secure=True, samesite='None',expires=expires)
        # Include token in data
        response.data = serializer.data
        return response
    
class LoginWiew(APIView):
    def post(self,request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = User.objects.filter(email=email).first()
            if user is None:
                raise AuthenticationFailed(['Email not found'])
            
            if not user.check_password(password):
                raise AuthenticationFailed(['Icorrect password'])
            
            payload = {
                'id': user.id,
                'name': user.email,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat':datetime.datetime.utcnow()
            }
            token = jwt.encode(payload,'secret',algorithm='HS256')
            response = Response()
            expires = datetime.datetime.utcnow() + datetime.timedelta(days=2)
            response.set_cookie(key='jwt', value=token, httponly=True, secure=True, samesite='None',expires=expires)
            response.data = {
                'jwt' : token
            }
            return response
        else:
        # If validation fails, return the validation errors
            return Response(serializer.errors, status=400)


class UserView(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated! no token provided')
        
        try :
            
            payload = jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated! a expirado')
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class VerifyPassword(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated! No se proporcionó ningún token.')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('No autenticado! El token ha expirado.')
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            user = User.objects.filter(id=payload['id']).first()
            if user:
                if not user.check_password(password):
                    raise AuthenticationFailed(['Contraseña incorrecta'])
            else:
                raise AuthenticationFailed('Usuario no encontrado')
        else:
            raise AuthenticationFailed('Datos inválidos')

        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Logout success'
        }
        return response