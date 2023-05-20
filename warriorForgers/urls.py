from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('mentors/', views.mentors, name='mentors'),
    path('about/', views.about, name='about'),
    
    
    path('accounts', include('accounts.urls')),
    path("dashboard/", include('dashboard.urls')),
]
