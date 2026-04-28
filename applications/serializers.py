from rest_framework import serializers
from .models import Application
from jobs.serializers import JobSerializer


class ApplicationSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(source='job.title', read_only=True)
    job_company = serializers.CharField(source='job.company', read_only=True)
    candidate_name = serializers.CharField(source='candidate.username', read_only=True)

    class Meta:
        model = Application
        fields = [
            'id', 'job', 'job_title', 'job_company',
            'candidate_name', 'status', 'cover_letter',
            'resume_link', 'created_at'
        ]
        read_only_fields = ['id', 'created_at', 'candidate_name', 'status']

    def validate(self, data):
        request = self.context['request']
        if Application.objects.filter(
            candidate=request.user,
            job=data['job']
        ).exists():
            raise serializers.ValidationError("You have already applied for this job.")
        return data

    def create(self, validated_data):
        validated_data['candidate'] = self.context['request'].user
        return super().create(validated_data)


class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['status']