from django.shortcuts import render, redirect
from accounts.models import Student, Mentor
from django.contrib.auth.models import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def student_register(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        field_type = request.POST['field_type']
        field_of_interest = request.POST['field_of_interest']
        
        student = Student.objects.create_user(
            username=email,
            email=email,
            field_type=field_type, 
            field_of_interest=field_of_interest
            )
        
        student.set_password(password)
        
        student.save()
        
        return redirect('dashboard')

    return render(request, 'accounts/student_register.html')


def login(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        student = auth.authenticate(username=email, password=password)
        
        if student is not None:
            
            auth.login(request, student)
            return redirect('/dashboard')
        else:
            return redirect('login')
    
    return render(request, 'accounts/student_login.html')

@login_required(login_url='/accounts/login')
def logout(request):
    auth.logout(request)    
    return redirect('/')