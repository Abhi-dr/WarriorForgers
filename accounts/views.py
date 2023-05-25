from django.shortcuts import render, redirect
from accounts.models import Student, Mentor
from django.contrib.auth.models import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def register(request):
    
    # if request.method == 'POST':
        # email = request.POST['email']
        # password = request.POST['password']
        # field_type = request.POST['field_type']
        # field_of_interest = request.POST['field_of_interest']
        
        # student = Student.objects.create_user(
        #     username=email,
        #     email=email,
        #     field_type=field_type, 
        #     field_of_interest=field_of_interest
        #     )
        
        # student.set_password(password)
        
        # student.save()
        
        # return redirect('dashboard')

    return render(request, 'accounts/register.html')


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

def student_register(request):
        
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        field_type = request.POST['field_type']
        field_of_interest = request.POST['field_of_interest']
        age = request.POST['age']
        
        student = Student.objects.create_user(
            username=email,
            first_name=email,
            age = age,
            email=email,
            field_type=field_type, 
            field_of_interest=field_of_interest
            )
        
        student.set_password(password)
        
        student.save()
        
        return redirect('login')
    
    else:
        return render(request, 'accounts/register.html')
    
def mentor_register(request):
        
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        age = request.POST['age']
        
        experties_field_type = request.POST['experties_field_type']
        experties_field_of_interest = request.POST['experties_field_of_interest']
        
        
        mentor = Mentor.objects.create_user(
            username=email,
            first_name=email,
            email=email,
            age = age,
            experties_field_type=experties_field_type,
            experties_field_of_interest=experties_field_of_interest
            )
        
        mentor.set_password(password)
        
        mentor.save()
        
        return redirect('login')
    
    else:
        return render(request, 'accounts/register.html')