from django.shortcuts import render, redirect
from accounts.models import Student, Mentor

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


def student_login(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        student = Student.objects.get(username=email)
        
        if student.check_password(password):
            return redirect('dashboard')
        else:
            return redirect('student_login')
    
    return render(request, 'accounts/student_login.html')