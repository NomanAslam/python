from django.shortcuts import render
from rest_framework import viewsets, status, permissions, generics
from .models import *
from .serializers import *
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.core.paginator import Paginator

from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({'status': False, 'message': serializer.errors}, status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username = serializer.data['username'], password = serializer.data['password'])
        if not user:
            return Response({'status': False, 'message': 'incorrect username or password'}, status.HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user=user)

        return Response({'status': True,'message': "User login", 'token': str(token)}, status.HTTP_201_CREATED)

class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data = data)
        if not serializer.is_valid():
            return Response({'status': False, 'message': serializer.errors}, status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response({'status': True,'message': "User Created"}, status.HTTP_201_CREATED)
        
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['GET'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerializer(emps, many=True, context={'request': request})
            return Response(emps_serializer.data)
        except Exception as e:
            return Response({
                'message': 'company does not exist'
            })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeViewSet2(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class QualificationViewSet(viewsets.ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer
    permission_classes = [permissions.IsAuthenticated]

class PeopleViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    http_method_names = ['get', 'post']

    def list(self, request):
        search = request.GET.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(name__startswith = search)

        serializer = PersonSerializer(queryset, many=True)
        return Response({'status': 200, 'data': serializer.data})
    
    @action(detail=True, methods=['GET'])
    def send_mail_to_person(self, request, pk):
        obj = Person.objects.get(pk=pk)
        serializer = PersonSerializer(obj)
        return Response({'status': True, 'message': 'Email sent successfully', 'data': serializer.data})

class PersonAPI(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        try:
            persons = Person.objects.all()
            page = request.GET.get('page', 1)
            page_size = 3
        
            paginator = Paginator(persons, page_size)
            serializer = PersonSerializer(paginator.page(page), many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'status': False, 'message': 'invalid page number'})
    
    def post(self, request):
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def put(self, request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(obj, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def patch(self, request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(obj, data = data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def delete(self, request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'Person deleted'})

@api_view(['GET', 'POST', 'PUT'])
def index(request):
    courses = {
            'course_name': 'Python',
            'learn': ['flask', 'django', 'Tarnado', 'FastAPI'],
            'course_provider': 'MultySol'
        }
    if request.method == 'GET':
        print(request.GET.get('search'))
        print('GET Method')
        return Response(courses)
    elif request.method == 'POST':
        data = request.data
        print(data)
        print('POST Method')
        return Response(courses)
    elif request.method == 'PUT':
        print('PUT Method')
        return Response(courses)
    
@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data = data)
    if serializer.is_valid():
        data = serializer.validated_data
        return Response({'message': 'success'})
    
    return Response(serializer.errors)
    
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):

    if request.method == 'GET':
        persons = Person.objects.filter(color__isnull = False)
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(obj, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(obj, data = data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'Person deleted'})
