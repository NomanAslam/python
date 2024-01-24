from django.urls import path
from .views import *

urlpatterns = [
    #path('', views.HelloAuthView.as_view(), name='hello_auth'),
    path('create/', CreateTodoAPIView.as_view(), name='create-todo'),
    path('list/', ListTodoAPIView.as_view(), name='create-list'),

    path('', TodosAPIView.as_view(), name='todos'),
    path('<int:id>', TodoDetailAPIView.as_view(), name='todos-detail'),
]