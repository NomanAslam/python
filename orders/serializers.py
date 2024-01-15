from .models import *
from rest_framework import serializers

class OrderCreationSerializer(serializers.ModelSerializer):

    size = serializers.CharField(max_length=20)
    order_status = serializers.HiddenField(default='Pending')
    quantity = serializers.IntegerField()

    class Meta:
        model = Order
        fields=['id', 'size', 'order_status', 'quantity']

class OrderDetailSerializer(serializers.ModelSerializer):

    size = serializers.CharField(max_length=20)
    order_status = serializers.CharField(default='Pending')
    quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Order
        fields=['id', 'size', 'order_status', 'quantity', 'created_at', 'updated_at']

class OrderStatusUpdateSerializer(serializers.ModelSerializer):

    order_status = serializers.CharField(default='Pending')

    class Meta:
        model = Order
        fields=['order_status']
