from django.shortcuts import render, redirect
from accounts.models import Mentor


def home(request):
    
    mentors = Mentor.objects.filter(ratings__gte=4.5)
    student = request.user
    
    parameters = {
        'mentors': mentors,
        'student': student
    }
    
    return render(request, 'home/home.html', parameters)

def courses(request):
    return render(request, 'courses.html')

def mentors(request):
    return render(request, 'mentors.html')

def about(request):
    return render(request, 'home/about.html')

