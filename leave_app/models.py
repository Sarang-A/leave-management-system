from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    department=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    

class LeaveType(models.Model):
    name=models.CharField(max_length=100)
    max_days=models.IntegerField()

    def __str__(self):
        return self.name
    

class Leave(models.Model):
    STATUS_CHOICES=[
        ('Pending','Pending'),
        ('Approved','Approved'),
        ('Rejected','Rejected'),
    ]

    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type=models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField()
    reason=models.TextField()
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    applied_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee} - {self.leave_type}"
    