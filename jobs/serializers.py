from rest_framework import serializers
from .models import Job, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class JobSerializer(serializers.ModelSerializer):
    recruiter_name = serializers.CharField(source='recruiter.username', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    is_expired = serializers.BooleanField(read_only=True)

    class Meta:
        model = Job
        fields = [
            'id', 'title', 'company', 'location', 'job_type',
            'experience', 'status', 'description', 'requirements',
            'salary_min', 'salary_max', 'deadline', 'recruiter_name',
            'category_name', 'is_expired', 'created_at'
        ]
        read_only_fields = ['id', 'created_at', 'recruiter_name']


class JobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'title', 'company', 'location', 'job_type', 'experience',
            'status', 'description', 'requirements', 'salary_min',
            'salary_max', 'deadline', 'category'
        ]

    def create(self, validated_data):
        validated_data['recruiter'] = self.context['request'].user
        return super().create(validated_data)