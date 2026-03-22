from django.contrib import admin
from .models import Employee,LeaveType,Leave
# Register your models here.
admin.site.register(Employee)
admin.site.register(LeaveType)
admin.site.register(Leave)