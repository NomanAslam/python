from rest_framework import serializers
from .models import *

from django.contrib.auth.models import User

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()                    #We can also use StringRelatedField, PrimaryKeyRelatedField, HyperLinkedRelatedField
    class Meta:
        model = Company
        fields = "__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"

class QualificationSerializer(serializers.HyperlinkedModelSerializer):
    qual_id = serializers.ReadOnlyField()
    class Meta:
        model = Qualification
        fields = "__all__"

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError('Username is taken')
            
        if data['email']:
            if User.objects.filter(email = data['email']).exists():
                raise serializers.ValidationError('Email is taken')
            
        return data
            
    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'], email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name']

class PersonSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    city = serializers.SerializerMethodField()
    #color_info = serializers.SerializerMethodField()
    class Meta:
        model = Person
        fields = "__all__"
        #depth = 1

    def get_city(self, obj):
        return "Isb"

    def get_color_info(self, obj):
        color_obj = Color.objects.get(id = obj.color.id)
        return {'color_name': color_obj.color_name, 'hex': '#000'}
    
    def validate(self, data):
        if len(data['name']) < 3:
            raise serializers.ValidationError('Name is too small')

        if data['age'] < 18:
            raise serializers.ValidationError('age should be greater than 18')
        return data