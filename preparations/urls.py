from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('quiz', views.quiz, name='quiz'),
    path('next/', views.next_question, name='next_question'),
    path('result/', views.result, name='result'),
    path('reset/', views.reset_quiz, name='reset_quiz'),
]