from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.ApplyJobView.as_view(), name='apply_job'),
    path('my/', views.MyApplicationsView.as_view(), name='my_applications'),
    path('job/<int:job_id>/', views.JobApplicationsView.as_view(), name='job_applications'),
    path('<int:pk>/status/', views.UpdateApplicationStatusView.as_view(), name='update_status'),
    path('<int:pk>/withdraw/', views.WithdrawApplicationView.as_view(), name='withdraw'),
]