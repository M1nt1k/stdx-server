from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import *

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer): 
    class Meta:
        model = Category
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Owner
        fields = '__all__'

class UniversitySerializer(serializers.ModelSerializer): 
    class Meta:
        model = University
        fields = '__all__'      

class TaskSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):    
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'taskType',
            # 'files',
            'universityTitle',
            'orderDate',
            'deliveryDate',
            'price',
            'is_published',
            'own'
        )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['own'] = instance.own.vk_id
        response['universityTitle'] = instance.universityTitle.name
        response['taskType'] = instance.taskType.name
        # response['files'] = instance.files.filesUrl
    
        return response
    
