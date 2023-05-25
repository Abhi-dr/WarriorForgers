from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('instructions/', views.instructions, name='instructions'),
    path('quiz', views.quiz, name='quiz'),
    path('next/', views.next_question, name='next_question'),
    path('result/', views.result, name='result'),
    path('reset/', views.reset_quiz, name='reset_quiz'),
    
    # =========== OLQ TEST ===========
    
    path('olq_test', views.olq_test, name='olq_test'),
]