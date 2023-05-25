from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from accounts.models import Student, Course, Mentor


@login_required(login_url='/accounts/login')
def home(request):   
    
    user = request.user
    student = get_object_or_404(Student, user_ptr=user)
    
    parameters = {
        'student': student
    }
    
    if student.is_registered == False:
        
        parameters = {
        'student': student
    }
        return render(request, 'dashboard/skill_test_blurred.html', parameters)
    
    else:
        return render(request, 'dashboard/home.html', parameters)
    
    
# ================================ REQUEST MEETING ================================

@login_required(login_url='/accounts/login')
def request_meeting(request):
        
    user = request.user
    student = get_object_or_404(Student, user_ptr=user)
    
    parameters = {
        'student': student
    }
    
    return render(request, 'dashboard/request_meeting.html', parameters)

# ================================ MY PROFILE ================================

@login_required(login_url='/accounts/login')
def my_profile(request):
            
    user = request.user
    student = get_object_or_404(Student, user_ptr=user)
    
    parameters = {
        'student': student
    }
    
    return render(request, 'dashboard/my_profile.html', parameters)

# ================================ MY COURSES ================================

@login_required(login_url='/accounts/login')
def my_courses(request):
                
    user = request.user
    student = get_object_or_404(Student, user_ptr=user)
    
    courses = student.courses.all()
    left_courses = Course.objects.exclude(id__in=courses)
    
    parameters = {
        'student': student,
        'courses': courses,
        'left_courses': left_courses
    }
    
    return render(request, 'dashboard/my_courses.html', parameters)


def buy_course(request, id):
    
    user = request.user
    student = get_object_or_404(Student, user_ptr=user)
    
    course = get_object_or_404(Course, id=id)
    
    student.courses.add(course)
    student.save()
    
    return redirect('my_courses')

# ================================ MY MENTORS ================================

@login_required(login_url='/accounts/login')
def my_mentors(request):
                        
    user = request.user
    student = get_object_or_404(Student, user_ptr=user)
    
    mentors = student.mentors.all()
    
    parameters = {
        'student': student,
        'mentors': mentors
    }
    
    return render(request, 'dashboard/my_mentors.html', parameters)