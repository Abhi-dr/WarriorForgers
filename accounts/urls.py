from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('register/', views.register, name='register'),
    
    path("student_register", views.student_register, name="student_register"),
    path("mentor_register", views.mentor_register, name="mentor_register"),
    
    path('login', views.login, name='login'),
    
    path('mentor_login', views.mentor_login, name='mentor_login'),
    path('student_login', views.student_login, name='student_login'),
    
    path('logout', views.logout, name='logout'),
]