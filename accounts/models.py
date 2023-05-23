from django.db import models
from django.contrib.auth.models import User

class Student(User):
    
    gender_choices = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    
    field_type_choices = (
        ("Commisioned Officer", "Commisioned Officer"),
        ("Non-Commisioned Officer", "Non-Commisioned Officer")
    )
    
    field_of_interest_choices = (
        ("NDA", "NDA"),
        ("CDS", "CDS"),
        ("Territorial Army", "Territorial Army"),
    )
         
    
    mobile_number = models.CharField(max_length=10, blank=True)
    
    registration_score = models.IntegerField(default=0)
    
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, blank=True, choices=gender_choices)
    highschool_score = models.IntegerField(default=0)
    intermediate_score = models.IntegerField(default=0)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    
    field_type = models.CharField(max_length=100, choices=field_type_choices, blank=True)
    field_of_interest = models.CharField(max_length=100, choices=field_of_interest_choices, blank=True)
    
    mentors = models.ManyToManyField('Mentor', blank=True)
    courses = models.ManyToManyField('Course', blank=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        verbose_name_plural = "Students"

class Mentor(User):
    mobile_number = models.CharField(max_length=10, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, blank=True)
    
    students = models.ManyToManyField('Student', blank=True)
    courses = models.ManyToManyField('Course', blank=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    
    class Meta:
        verbose_name_plural = "Mentors"
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='course_pics', blank=True)
    
    students = models.ManyToManyField('Student', blank=True)
    mentors = models.ManyToManyField('Mentor', blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Courses"