from django.db import models
from accounts.models import Student, Mentor

class Meeting(models.Model):
    domain = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    question = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Meeting with {self.mentor.first_name} { self.mentor.last_name } on {self.date} at {self.time}"