from django.shortcuts import render, redirect
from accounts.models import Mentor
from accounts.models import Student
from django.shortcuts import get_object_or_404

def home(request):
    
    mentors = Mentor.objects.filter(ratings__gte=4.5)
    
    user = request.user
    
    if user.is_authenticated:
    
        student = get_object_or_404(Student, user_ptr=user)
    
        parameters = {
            'mentors': mentors,
            'student': student,
            
        }
    
    else:
            
        parameters = {
            'mentors': mentors
        }
        
    return render(request, 'home/home.html', parameters)

def courses(request):
    return render(request, 'courses.html')

def mentors(request):
    return render(request, 'mentors.html')

def about(request):
    return render(request, 'home/about.html')

