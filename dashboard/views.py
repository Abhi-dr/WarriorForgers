from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from accounts.models import Student, Course, Mentor, Video


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
        return render(request, 'dashboard/student/skill_test_blurred.html', parameters)
    
    else:
        
        courses = student.courses.all()
        left_mentors = Mentor.objects.exclude(id__in=student.mentors.all().values_list('id'))
        
        parameters = {
        'student': student,
        'courses': courses,
        'left_mentors': left_mentors
    }
        
        return render(request, 'dashboard/student/home.html', parameters)
    
    
# ================================ REQUEST MEETING ================================

@login_required(login_url='/accounts/login')
def request_meeting(request):
        
    user = request.user
    student = get_object_or_404(Student, user_ptr=user)
    
    parameters = {
        'student': student
    }
    
    return render(request, 'dashboard/student/request_meeting.html', parameters)

# ================================ MY PROFILE ================================

@login_required(login_url='/accounts/login')
def my_profile(request):
            
    user = request.user
    student = get_object_or_404(Student, user_ptr=user)
    
    parameters = {
        'student': student
    }
    
    return render(request, 'dashboard/student/my_profile.html', parameters)

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
    
    return render(request, 'dashboard/student/my_courses.html', parameters)


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
    
    return render(request, 'dashboard/student/my_mentors.html', parameters)

# MENTOR DASHBOARD

@login_required(login_url='/accounts/login')
def mentor_dashboard(request):
                            
    user = request.user
    mentor = get_object_or_404(Mentor, user_ptr=user)
    
    parameters = {
        'mentor': mentor
    }
    
    return render(request, 'dashboard/mentor/home.html', parameters)

# ================================ MENTOR VIDEOS ================================

@login_required(login_url='/accounts/login')
def mentor_videos(request):
                        
    user = request.user
    student = get_object_or_404(Student, user_ptr=user)
    
    mentors = student.mentors.all()
    videos = Video.objects.filter(mentor__in=mentors)
    
    parameters = {
        'student': student,
        'videos': videos
    }
    
    return render(request, 'dashboard/student/mentor_videos.html', parameters)

# ================================ CONNECT MENTOR ================================

@login_required(login_url='/accounts/login')
def connect_mentor(request, id):
        
    user = request.user
    student = get_object_or_404(Student, user_ptr=user)
    
    mentor = get_object_or_404(Mentor, id=id)
    
    student.mentors.add(mentor)
    student.save()
    
    return redirect('my_mentors')

# ================================ SSB INFO ================================

@login_required(login_url='/accounts/login')
def ssb_info(request):
            
        user = request.user
        student = get_object_or_404(Student, user_ptr=user)
        
        parameters = {
            'student': student
        }
        
        return render(request, 'dashboard/student/ssb_info.html', parameters)   