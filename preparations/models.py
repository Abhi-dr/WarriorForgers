from django.db import models

class Registration_Quiz(models.Model):
    question = models.CharField(max_length=1000)
    option1 = models.CharField(max_length=1000)
    option2 = models.CharField(max_length=1000)
    option3 = models.CharField(max_length=1000)
    option4 = models.CharField(max_length=1000)
    
    answer_choices = (
        ("option1", "option1"),
        ("option2", "option2"),
        ("option3", "option3"),
        ("option4", "option4"),
    )
    
    answer = models.CharField(max_length=1000, choices=answer_choices)
    
    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name_plural = "Registration_Quiz"
    
    