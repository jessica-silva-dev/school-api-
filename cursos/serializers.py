from rest_framework import serializers
from .models import Course, Assessment

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = [
            'id',
            'course', 
            'name', 
            'email', 
            'comments', 
            'assessment', 
            'active', 
            'created_at'
        ]
        extra_kwargs = {
            'email': {'write_only': True}
        }
        
class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'url',
            'active',
            'created_at',
        ]