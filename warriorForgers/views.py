from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')

def courses(request):
    return render(request, 'courses.html')

def mentors(request):
    return render(request, 'mentors.html')

def about(request):
    return render(request, 'about.html')

