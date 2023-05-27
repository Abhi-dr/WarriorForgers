from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.mentor_home, name='mentor_dashboard'),
    
    path('mentor_my_profile/', views.mentor_my_profile, name='mentor_my_profile'),
    path('mmentor_my_courses/', views.mentor_my_courses, name='mentor_my_courses'),
    path('mentor_my_videos/', views.mentor_my_videos, name='mentor_my_videos'),
    
    path('mentor_registered_students', views.mentor_registered_students, name='mentor_registered_students'),
       
]