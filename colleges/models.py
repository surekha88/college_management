from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import UserManager


# Create your models here.
#Class for Custom User
class CustomUser(AbstractUser):
    USER_TYPE = ((1, "Super_Admin"), (2, "Teacher"), (3, "Student"))
    GENDER = [("M", "Male"), ("F", "Female")]
    email = models.EmailField(max_length=50,null=False,blank=False,default = '')
    user_type = models.CharField(default=1, choices=USER_TYPE, max_length=1)
    gender = models.CharField(max_length=1, choices=GENDER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #objects = UserManager()

#Model for Super_Admin
class Super_Admin(models.Model):
    USER_TYPE = ((1, "Super_Admin"), (2, "Teacher"), (3, "Student"))
    id = models.AutoField(primary_key=True)
    #admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    name = models.CharField(max_length=200,null=False,blank=False,default = '')
    email = models.EmailField(max_length=50,null=False,blank=False,default = '')
    user_type = models.CharField(default=1, choices=USER_TYPE, max_length=1)
    objects = UserManager()
#Model for Teacher
class Teacher(models.Model):
    USER_TYPE = ((1, "Super_Admin"), (2, "Teacher"), (3, "Student"))
    id = models.AutoField(primary_key=True)
    #admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    name = models.CharField(max_length=200,null=False,blank=False,default = '')
    email = models.EmailField(max_length=50,null=False,blank=False,default = '')
    user_type = models.CharField(default=2, choices=USER_TYPE, max_length=1)
    objects = UserManager()
    
#Model for Student
class Student(models.Model):
    USER_TYPE = ((1, "Super_Admin"), (2, "Teacher"), (3, "Student"))
    id = models.AutoField(primary_key=True)
    #admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    name = models.CharField(max_length=200,null=False,blank=False,default = '')
    email = models.EmailField(max_length=50,null=False,blank=False,default = '')
    user_type = models.CharField(default=3, choices=USER_TYPE, max_length=1)
    objects = UserManager()
    

