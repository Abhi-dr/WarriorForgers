from django.contrib import admin
from .models import Meeting

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ['student', 'mentor', 'date', 'time', 'approved']
    list_filter = ['approved', 'mentor', 'student']
    search_fields = ['student', 'mentor', 'date', 'time']
    list_per_page = 20