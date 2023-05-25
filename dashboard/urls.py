from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='dashboard'),
    
    path('regustration_quiz/', include('preparations.urls')),
    path('preparations/', include('preparations.urls')),
    
    path('request_meeting', views.request_meeting, name='request_meeting'),
       
]