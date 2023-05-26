from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='dashboard'),
    
    path('/mentor_dashboard', views.mentor_dashboard, name='mentor_dashboard'),
    
    path('regustration_quiz/', include('preparations.urls')),
    path('preparations/', include('preparations.urls')),
    
    path('request_meeting', views.request_meeting, name='request_meeting'),
    path('my_profile', views.my_profile, name='my_profile'),
    path('my_courses', views.my_courses, name='my_courses'),
    path('my_mentors', views.my_mentors, name='my_mentors'),
    path('mentor_videos', views.mentor_videos, name='mentor_videos'),
    
    path('ssb_info', views.ssb_info, name='ssb_info'),
    
    # ====================== FUNCTIONALITIES ======================
    
    path('buy_course/<int:id>', views.buy_course, name='buy_course'),
    path('connect_mentor/<int:id>', views.connect_mentor, name='connect_mentor'),
       
]