from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, Responses, Category, University

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'tasks']

class UniversitySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = University
        fields = ['id', 'name', 'owner', 'tasks']

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    responces = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'category', 'university', 'orderDate', 'deliveryDate', 'is_published', 'owner', 'responces']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['university'] = instance.university.name
        response['category'] = instance.category.name

        return response

class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    responces = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    category = serializers.ReadOnlyField(source='category.name')
    university = serializers.ReadOnlyField(source='university.name')

    class Meta:
        model = User
        fields = ['id', 'username', 'tasks', 'responces', 'category', 'university']

class ResponsesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Responses
        fields = ['id', 'about', 'price', 'deliveryDate', 'owner', 'task']