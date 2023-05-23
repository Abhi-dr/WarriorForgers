from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('student_register/', views.student_register, name='student_register'),
    path('login', views.login, name='login'),
    
    path('logout', views.logout, name='logout'),
]