from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from learning.serializers import *
from learning.models import *
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from learning.helpers import save_pdf

class GeneratePdf(APIView):
    def get(self, request):
        student_obj = Student.objects.all()
        params = {
            #'today': datetime.date.today(),
            'student_objs': student_obj
        }
        file_name, status = save_pdf(params)

        if not status:
            return Response({'status': 400})
        
        return Response({'status': 200, 'path': f'/media/{file_name}.pdf'})

class StudentGeneric(generics.ListAPIView, generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class StudentGenericNew(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    lookup_field = 'id'

@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    if request.method == 'GET':
        drinks = Drink.objects.all()                        #Get all the drinks
        serializer = DrinkSerializer(drinks, many=True)     #Serialize them
        #return JsonResponse(serializer.data, safe=False)
        return JsonResponse({"drink": serializer.data})     #Return json
    
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'status' : status.HTTP_201_CREATED, 'description': 'success'})
    
        return Response({'error': serializer.errors, 'status': status.HTTP_403_FORBIDDEN, 'description': 'error'})

@api_view(['GET', 'PUT', 'DELETE'])    
def drink_details(request, id, format=None):

    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
    
class RegisterUser(APIView):
    def post(self, request):
        #return Response({'status': status.HTTP_403_FORBIDDEN, 'description': 'error'})

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username = serializer.data['username'])
            #token, _ = Token.objects.get_or_create(user=user)
            refresh = RefreshToken.for_user(user)
            return Response({'data': serializer.data, 'status' : status.HTTP_201_CREATED, 'refresh': str(refresh), 
                             'access': str(refresh.access_token), 'description': 'success'})
    
        return Response({'error': serializer.errors, 'status': status.HTTP_403_FORBIDDEN, 'description': 'error'})


class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentModelSerializer

    def get(self, request):
        student = Student.objects.all()
        serializer = self.serializer_class(student, many=True)
        return Response({'data': serializer.data, 'status' : status.HTTP_201_CREATED, 'description': 'success'})
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'status' : status.HTTP_201_CREATED, 'description': 'success'})
        return Response({'error': serializer.errors, 'status' : status.HTTP_201_CREATED, 'description': 'success'})

def homePage(request):
    data = {
        'title': 'Home Page',
        'clist': ['PHP', 'Java', 'Django'],
        'studentsList': [
            {'name': "Ali", 'phone': "0300123"},
            {'name': "Waqas", 'phone': "0300456"},
            {'name': "Shahid", 'phone': "0300789"},
        ],
        'numbers': [10, 20, 30, 40, 50],
    }
    return render(request, "index.html", data)

class StudentView(APIView):
    serializer_class = StudentModelSerializer

    def get(self, request):
        student = Student.objects.all()
        serializer = self.serializer_class(student, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("object is created!")
        return Response(serializer.errors)
    
class TeacherView(APIView):
    serializer_class = TeacherModelSerializer

    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = self.serializer_class(teacher, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if (serializer.is_valid):
            serializer.save()
            return Response("object is created!")
        return Response(serializer.errors)
    
class UniversityView(APIView):
    #serializer_class = UniversityModelSerializer
    serializer = UniversitySerializer

    def get(self, request):
        university = University.objects.all()
        serializer = self.serializer(university, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer(data = request.data)
        if (serializer.is_valid):
            serializer.save()
            return Response("object is created!")
        return Response(serializer.errors)
