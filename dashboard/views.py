from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from accounts.models import Student, Course, Mentor, Video
from dashboard.models import Meeting


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
        meeetings = Meeting.objects.filter(student=student)[::-1]
        
        parameters = {
        'student': student,
        'courses': courses,
        'left_mentors': left_mentors,
        'meetings': meeetings
    }
        
        return render(request, 'dashboard/student/home.html', parameters)
    
    
# ================================ REQUEST MEETING ================================

@login_required(login_url='/accounts/login')
def request_meeting(request):
        
    user = request.user
    student = get_object_or_404(Student, user_ptr=user)
    
    mentors = student.mentors.all()
    
    if request.method == "POST":
        
        domain = request.POST.get('domain')
        mentor_id = request.POST.get('mentor_id')
        question = request.POST.get('question')
        date = request.POST.get('date')
        time = request.POST.get('time')
        
        mentor = get_object_or_404(Mentor, id=mentor_id)
        
        meeting = Meeting(student=student, mentor=mentor, date=date, time=time, question=question, domain=domain)
        meeting.save()
        
        return redirect('request_meeting')
    
    parameters = {
        'student': student,
        'mentors': mentors
    }
    
    return render(request, 'dashboard/student/request_meeting.html', parameters)

# ================================ MY PROFILE ================================

@login_required(login_url='/accounts/login')
def my_profile(request):
    
    user = request.user
    student = get_object_or_404(Student, user_ptr=user)
    
    if request.method == "POST":
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        highschool_score = request.POST.get('hignschool_score')
        intermediate_score = request.POST.get('intermediate_score')
        
        student.first_name = first_name
        student.last_name = last_name
        student.email = email
        student.mobile_number = mobile_number
        student.age = age
        student.gender = gender
        student.highschool_score = highschool_score
        student.intermediate_score = intermediate_score
        
        student.save()
        
        return redirect('my_profile')
            
    
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
    
# ================================ EDIT PROFILE ================================

@login_required(login_url='/accounts/login')
def edit_profile(request):
                
    user = request.user
    student = get_object_or_404(Student, user_ptr=user)
    
    
    parameters = {
        'student': student
    }
    
    return render(request, 'dashboard/student/edit_profile.html', parameters)