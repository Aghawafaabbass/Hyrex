from rest_framework import generics, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from .models import Job, Category
from .serializers import JobSerializer, JobCreateSerializer, CategorySerializer


class JobListView(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'company', 'location', 'description']
    ordering_fields = ['created_at', 'salary_min', 'salary_max']

    def get_queryset(self):
        queryset = Job.objects.filter(status='active')
        job_type = self.request.query_params.get('job_type')
        experience = self.request.query_params.get('experience')
        category = self.request.query_params.get('category')
        location = self.request.query_params.get('location')

        if job_type:
            queryset = queryset.filter(job_type=job_type)
        if experience:
            queryset = queryset.filter(experience=experience)
        if category:
            queryset = queryset.filter(category__slug=category)
        if location:
            queryset = queryset.filter(location__icontains=location)
        return queryset


class JobDetailView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [AllowAny]


class JobCreateView(generics.CreateAPIView):
    serializer_class = JobCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.user_type != 'recruiter':
            raise PermissionDenied("Only recruiters can post jobs.")
        serializer.save(recruiter=self.request.user)


class JobUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Job.objects.filter(recruiter=self.request.user)


class RecruiterJobsView(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Job.objects.filter(recruiter=self.request.user)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]