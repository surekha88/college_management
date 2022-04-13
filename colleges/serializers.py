from rest_framework import serializers
from .models import *
#Serializers for all the models
class Super_Admin_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Super_Admin
        fields = '__all__'

class Teacher_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
