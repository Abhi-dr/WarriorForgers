from django.contrib import admin
from .models import Registration_Quiz, OLQ_Quiz

@admin.register(Registration_Quiz)
class Registration_QuizAdmin(admin.ModelAdmin):
    list_display = ('question', 'option1', 'option2', 'option3', 'option4', 'answer')
    
@admin.register(OLQ_Quiz)
class OLQ_QuizAdmin(admin.ModelAdmin):
    list_display = ('question', 'option1', 'option2', 'option3', 'option4', 'answer')