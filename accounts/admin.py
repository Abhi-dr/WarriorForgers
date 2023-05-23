from django.contrib import admin
from .models import Student, Mentor, Course

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mobile_number', 'registration_score', 'highschool_score', 'intermediate_score')
    
    exclude = ('password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'is_staff', 'is_active')
    
@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mobile_number')
    exclude = ('password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'is_staff', 'is_active')
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

    