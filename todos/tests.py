from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import *

#Class for Common Functions
class TodosAPITestCase(APITestCase):
    def create_todo(self):
        sample_todo = {'title': 'Hello', 'desc': 'Hello Des'}
        return self.client.post(reverse('todos'), sample_todo)
    
    def authenticate(self):
        self.client.post(reverse('sign_up'), {'username': 'username', 'phone_number': '+923001234567', 'email': 'email@gmail.com', 'password': 'password'})
        response = self.client.post(reverse('login'), {'email': 'email@gmail.com', 'password': 'password'})

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + response.data['token'])

#Tests for ListCreateTodos
class TestListCreateTodos(TodosAPITestCase):

    def test_should_not_creates_todo_with_no_auth(self):
        response = self.create_todo()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_should_create_todo(self):
        previous_todos_count = Todo.objects.all().count()
        self.authenticate()
        response = self.create_todo()
        self.assertEqual(Todo.objects.all().count(), previous_todos_count + 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Hello')
        self.assertEqual(response.data['desc'], 'Hello Des')

    def test_retrieves_all_todos(self):
        self.authenticate()
        response = self.client.get(reverse('todos'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['results'], list)

        self.create_todo()

        response2 = self.client.get(reverse('todos'))
        self.assertIsInstance(response2.data['count'], int)
        self.assertEqual(response2.data['count'], 1)

#Tests for List, Update, Delete
class TestTodoDetailAPIView(TodosAPITestCase):

    def test_retrieves_one_item(self):
        self.authenticate()
        response = self.create_todo()

        res = self.client.get(reverse('todos-detail', kwargs={'id': response.data['id']}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        todo = Todo.objects.get(id=response.data['id'])
        self.assertEqual(todo.title, res.data['title'])

    def test_updates_one_item(self):
        self.authenticate()
        response = self.create_todo()

        res = self.client.patch(reverse('todos-detail', kwargs={'id': response.data['id']}), {'title': 'New One', 'is_complete': True})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.get(id=response.data['id']).is_complete, True)
        self.assertEqual(Todo.objects.get(id=response.data['id']).title, 'New One')

    def test_deletes_one_item(self):
        self.authenticate()
        res = self.create_todo()
        prv_db_count = Todo.objects.all().count()

        self.assertGreater(prv_db_count, 0)
        self.assertEqual(prv_db_count, 1)

        response = self.client.delete(reverse('todos-detail', kwargs={'id': res.data['id']}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Todo.objects.all().count(), 0)
