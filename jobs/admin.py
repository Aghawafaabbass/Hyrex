from django.contrib import admin
from .models import Job, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'recruiter', 'job_type', 'experience', 'status', 'created_at')
    list_filter = ('job_type', 'experience', 'status', 'category')
    search_fields = ('title', 'company', 'location')
    list_editable = ('status',)
    date_hierarchy = 'created_at'