from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from accounts.models import Student


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