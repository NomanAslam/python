from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import *
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate

class HelloAuthView(generics.GenericAPIView):

    @swagger_auto_schema(operation_summary="Hello Auth Test API")    
    def get(self, response):
        return Response(data={'message': 'Hello Auth'}, status=status.HTTP_200_OK)
    
#http://127.0.0.1:8000/authentication/signup/
class UserCreateView(generics.GenericAPIView):
    serializer_class = UserCreationSerializer
    permission_classes = []
    authentication_classes = []

    @swagger_auto_schema(operation_summary="Create a User Account")
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Errors may be send based on Serializer fields
    
#http://127.0.0.1:8000/authentication/login/
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = []
    authentication_classes = []

    @swagger_auto_schema(operation_summary="Create a User Account")
    def post(self, request):

        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(username=email, password=password)
        if user:
            serializer = self.serializer_class(user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    

#http://127.0.0.1:8000/authentication/login/
class AuthUserAPIView(generics.GenericAPIView):
    serializer_class = UserCreationSerializer
    #permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(operation_summary="Create a User Account")
    def get(self, request):
        user = request.user
        serializer = UserCreationSerializer(user)
        return Response({'data': serializer.data})