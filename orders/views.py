from django.shortcuts import render, get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema

User = get_user_model()

class HelloOrderView(generics.GenericAPIView):

    @swagger_auto_schema(operation_summary="Hello Orders Test API")
    def get(self, response):
        return Response(data={'message': 'Hello Orders'}, status=status.HTTP_200_OK)
    
# http://127.0.0.1:8000/orders/
class OrderCreateListView(generics.GenericAPIView):
    serializer_class = OrderCreationSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(operation_summary="List of Orders")
    def get(self, request):
        orders = Order.objects.all()
        serializer = self.serializer_class(instance=orders, many=True) 
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Create a new Order")
    def post(self, request):
        user = request.user
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# http://127.0.0.1:8000/orders/1
class OrderDetailView(generics.GenericAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(operation_summary="Retrieve an Order by id")
    def get(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Update an Order by id")
    def put(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(instance=order, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Remove/Delete an Order by id")
    def delete(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# http://127.0.0.1:8000/orders/update-status/1
class UpdateOrderStatus(generics.GenericAPIView):
    serializer_class = OrderStatusUpdateSerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(operation_summary="Update an Order Status")
    def put(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(instance=order, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# http://127.0.0.1:8000/orders/user/1/orders/
class UserOrdersViews(generics.GenericAPIView):
    serializer_class = OrderDetailSerializer
    #permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()

    @swagger_auto_schema(operation_summary="Get all Orders for a User")
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        orders = Order.objects.all().filter(customer=user)
        serializer = self.serializer_class(instance=orders, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

# http://127.0.0.1:8000/orders/user/1/order/1/
class UserOrderDetailViews(generics.GenericAPIView):
    serializer_class = OrderDetailSerializer
    #permission_classes = [IsAuthenticated]
    #queryset = Order.objects.all()

    @swagger_auto_schema(operation_summary="Get a user's specific order")
    def get(self, request, user_id, order_id):
        user = User.objects.get(pk=user_id)
        order = Order.objects.all().filter(customer=user).get(pk=order_id)
        serializer = self.serializer_class(instance=order)

        return Response(data=serializer.data, status=status.HTTP_200_OK)