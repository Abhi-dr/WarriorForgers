from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='main_home'),
    path('courses/', views.courses, name='courses'),
    path('mentors/', views.mentors, name='mentors'),
    path('about/', views.about, name='main_about'),
    
    
    path('accounts/', include('accounts.urls')),
    path("dashboard/", include('dashboard.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)