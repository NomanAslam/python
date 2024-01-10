from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'qualifications', QualificationViewSet)
router.register(r'peoples', PeopleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('index/', index),
    path('person/', person),
    path('login/', login),
    path('persons/', PersonAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('logins/', LoginAPI.as_view()),
]