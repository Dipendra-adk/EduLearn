from rest_framework import serializers
from .models import User, Instructor, Learner
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LearnerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = Learner
        fields = '__all__'

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        categories = validated_data.pop('interested_categories')
        user = User.objects.create_user(email=email, password=password, role='learner')
        learner = Learner.objects.create(user=user, **validated_data)
        learner.interested_categories.set(categories)
        return learner

class InstructorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = Instructor
        fields = '__all__'

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        user = User.objects.create_user(email=email, password=password, role='instructor')
        instructor = Instructor.objects.create(user=user, **validated_data)
        return instructor   