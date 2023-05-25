from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='dashboard'),
    
    path('regustration_quiz/', include('preparations.urls')),
    path('preparations/', include('preparations.urls')),
    
    path('request_meeting', views.request_meeting, name='request_meeting'),
    path('my_profile', views.my_profile, name='my_profile'),
    path('my_courses', views.my_courses, name='my_courses'),
    path('my_mentors', views.my_mentors, name='my_mentors'),
       
]