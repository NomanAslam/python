from rest_framework import serializers
from learning.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    standard = serializers.IntegerField()

class TeacherSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    firstName = serializers.CharField(max_length=100)
    lastName = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

class UniversitySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    uniName = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class TeacherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class UniversityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "__all__"

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = "__all__"

    def validate(self, data):
        if data['quality'] < 5:
            raise serializers.ValidationError({'error': 'Quality is less than five'})
        
        elif has_numbers((data['name'])):
            raise serializers.ValidationError({'error': 'Name contains number'})
        
        return data
    
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)