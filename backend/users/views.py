from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import InstructorSerializer, LearnerSerializer
from .models import Instructor, Learner
class InstructorView(APIView):
    def get(self, request):
        instructor=Instructor.objects.all()
        serializer=InstructorSerializer(instructor, many=True)
        return Response(serializer.data)
    
class LearnerView(APIView):
    def get(self, request):
        learner=Learner.objects.all()
        serializer=LearnerSerializer(learner, many=True)        
        return Response(serializer.data)    