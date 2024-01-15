from django.shortcuts import render, get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from .models import *
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from django.contrib.auth import get_user_model

User = get_user_model()

class HelloOrderView(generics.GenericAPIView):
    def get(self, response):
        return Response(data={'message': 'Hello Orders'}, status=status.HTTP_200_OK)
    
# http://127.0.0.1:8000/orders/
class OrderCreateListView(generics.GenericAPIView):
    serializer_class = serializers.OrderCreationSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        orders = Order.objects.all()
        serializer = self.serializer_class(instance=orders, many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        user = request.user

        if serializer.is_valid():
            serializer.save(customer=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# http://127.0.0.1:8000/orders/1
class OrderDetailView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    permission_classes = [IsAdminUser]

    def get(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, order_id):
        data = request.data

        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(data=data, instance=order)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# http://127.0.0.1:8000/orders/update-status/1
class UpdateOrderStatus(generics.GenericAPIView):
    serializer_class = serializers.OrderStatusUpdateSerializer
    permission_classes = [IsAdminUser]

    def put(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        data = request.data
        serializer = self.serializer_class(data=data, instance=order)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# http://127.0.0.1:8000/orders/user/1/orders/
class UserOrdersViews(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    #permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()

    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        orders = Order.objects.all().filter(customer=user)
        serializer = self.serializer_class(instance=orders, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

# http://127.0.0.1:8000/orders/user/1/order/1/
class UserOrderDetailViews(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    #permission_classes = [IsAuthenticated]
    #queryset = Order.objects.all()

    def get(self, request, user_id, order_id):
        user = User.objects.get(pk=user_id)
        order = Order.objects.all().filter(customer=user).get(pk=order_id)
        serializer = self.serializer_class(instance=order)

        return Response(data=serializer.data, status=status.HTTP_200_OK)