from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


# Create your views here.
#Defining Viewsets for the models
class Super_Admin_Viewset(viewsets.ModelViewSet):
    queryset = models.Super_Admin.objects.all()
    serializer_class = serializers.Super_Admin_Serializer
    
class Teacher_Viewset(viewsets.ModelViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.Teacher_Serializer

class Student_Viewset(viewsets.ReadOnlyModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.Student_Serializer
