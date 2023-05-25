from django.contrib import admin
from django.urls import path, include
from . import views, olq_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('instructions/', views.instructions, name='instructions'),
    path('quiz', views.quiz, name='quiz'),
    path('next/', views.next_question, name='next_question'),
    path('result/', views.result, name='result'),
    path('reset/', views.reset_quiz, name='reset_quiz'),
    
    # =========== OLQ TEST ===========
    
    path('olq_test', olq_views.olq_test, name='olq_test'),
    
    path('olq_instructions/', olq_views.olq_instructions, name='olq_instructions'),
    path('olq_quiz', olq_views.olq_quiz, name='olq_quiz'),
    path('olq_next/', olq_views.olq_next_question, name='olq_next_question'),
    path('olq_result/', olq_views.olq_result, name='olq_result'),
    path('olq_reset/', olq_views.olq_reset_quiz, name='olq_reset_quiz'),
    
    # =========== MOCK TEST ===========
    
    path('mock_test', views.mock_test, name='mock_test'),
]