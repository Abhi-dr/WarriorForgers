from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from accounts.models import Student, Course, Mentor, Video


@login_required(login_url='/accounts/login')
def mentor_home(request):   
    
    user = request.user
    mentor = get_object_or_404(Mentor, user_ptr=user)
    
    parameters = {
        'mentor': mentor
    }
            
    parameters = {
        'mentor': mentor
    }
    return render(request, 'dashboard/mentor/home.html', parameters)
    
@login_required(login_url='/accounts/login')
def mentor_my_profile(request):
    user = request.user
    mentor = get_object_or_404(Mentor, user_ptr=user)
    
    parameters = {
        'mentor': mentor
    }
    return render(request, 'dashboard/mentor/my_profile.html', parameters)

@login_required(login_url='/accounts/login')
def mentor_my_courses(request):
    user = request.user
    mentor = get_object_or_404(Mentor, user_ptr=user)
    
    courses = Course.objects.filter(mentor=mentor)
    
    parameters = {
        'mentor': mentor,
        'courses': courses
    }
    return render(request, 'dashboard/mentor/my_courses.html', parameters)

@login_required(login_url='/accounts/login')
def mentor_my_videos(request):
    user = request.user
    mentor = get_object_or_404(Mentor, user_ptr=user)
    
    videos = Video.objects.filter(mentor=mentor)
    
    parameters = {
        'mentor': mentor,
        'videos': videos
    }
    return render(request, 'dashboard/mentor/my_videos.html', parameters)

@login_required(login_url='/accounts/login')
def mentor_registered_students(request):
    user = request.user
    mentor = get_object_or_404(Mentor, user_ptr=user)
    
    students = Student.objects.filter(mentor=mentor)
    
    parameters = {
        'mentor': mentor,
        'students': students
    }
    return render(request, 'dashboard/mentor/registered_students.html', parameters)
