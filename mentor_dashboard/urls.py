from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.mentor_home, name='mentor_dashboard'),
    
    path('mentor_my_profile/', views.mentor_my_profile, name='mentor_my_profile'),
    path('mmentor_y_courses/', views.mentor_my_courses, name='mentor_my_courses'),
    path('mentor_my_videos/', views.mentor_my_videos, name='mentor_my_videos'),
       
]