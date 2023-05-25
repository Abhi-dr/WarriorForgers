from django.db import models

class Registration_Quiz(models.Model):
    question = models.CharField(max_length=1000)
    option1 = models.CharField(max_length=1000)
    option2 = models.CharField(max_length=1000)
    option3 = models.CharField(max_length=1000)
    option4 = models.CharField(max_length=1000)
    
    answer = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name_plural = "Registration_Quiz"

# ============================= OLQ TEST ==========================

class OLQ_Quiz(models.Model):
    question = models.CharField(max_length=1000)
    option1 = models.CharField(max_length=1000)
    option2 = models.CharField(max_length=1000)
    option3 = models.CharField(max_length=1000)
    option4 = models.CharField(max_length=1000)
    
    answer = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name_plural = "OLQ_Quiz"