from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobListView.as_view(), name='job_list'),
    path('<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
    path('create/', views.JobCreateView.as_view(), name='job_create'),
    path('<int:pk>/update/', views.JobUpdateDeleteView.as_view(), name='job_update'),
    path('my-jobs/', views.RecruiterJobsView.as_view(), name='recruiter_jobs'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
]