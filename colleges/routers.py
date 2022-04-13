from .views import *
from rest_framework import routers
from django.urls import path, include
#Routers to automatically generate router configuration
router = routers.DefaultRouter()
router.register(r'Super_Admin', Super_Admin_Viewset,basename = 'Super_Admin')
router.register(r'Teacher', Teacher_Viewset, basename = 'Teacher')
router.register(r'Student', Student_Viewset,basename = 'Student')

urlpatterns = [
    path('', include(router.urls)),
]
