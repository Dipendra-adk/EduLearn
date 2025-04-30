from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from users.serializers import InstructorSerializer, LearnerSerializer
from .models import Instructor, Learner
from rest_framework import permissions

class InstructorList(generics.ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    permission_classes = [permissions.IsAuthenticated]

class InstructorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class LearnerList(generics.ListCreateAPIView):
    queryset = Learner.objects.all()
    serializer_class = LearnerSerializer  
    permission_classes = [permissions.IsAuthenticated]

class LearnerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Learner.objects.all()
    serializer_class = LearnerSerializer
    permission_classes = [permissions.IsAuthenticated]