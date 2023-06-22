from django.db import models

class AdminData(models.Model):
    course_name=models.CharField(max_length=100)
    fee=models.IntegerField()
    institute=models.CharField(max_length=100)
    trainer_name=models.CharField(max_length=100)
    date=models.DateField()
    trainer_mode=models.CharField(max_length=100)

class studentsData(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email_id=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    course=models.EmailField(max_length=100)
    qualification=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

class studentfeedbackData(models.Model):
    user_name = models.CharField(max_length=100)
    comment=models.CharField(max_length=100)
    date=models.DateTimeField(max_length=100)
