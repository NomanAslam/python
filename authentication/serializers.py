from .models import *
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=80)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']

    def validate(self, attr):
        username_exists = User.objects.filter(username=attr['username']).exists()
        if (username_exists):
            raise serializers.ValidationError(detail='Username already exists')
        
        email_exists = User.objects.filter(email=attr['email']).exists()
        if (email_exists):
            raise serializers.ValidationError(detail='Email already exists')
        
        phone_number_exists = User.objects.filter(phone_number=attr['phone_number']).exists()
        if (phone_number_exists):
            raise serializers.ValidationError(detail='Phone number already exists')
        
        return super().validate(attr)
    
    def create(self, validated_data):
        
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            phone_number = validated_data['phone_number']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
