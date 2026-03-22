from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Employee
from django.contrib.auth.decorators import login_required
from .forms import Leaveform
from .models import Leave

# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        department=request.POST['department']
        designation=request.POST['designation']

        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{'error':'Username already exists'})

        user=User.objects.create_user(
            username=username,
            password=password
        )

        Employee.objects.create(
            user=user,
            department=department,
            designation=designation
        )

        return redirect('login')
    return render(request,'register.html')



def user_login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request,'login.html')    



def user_logout(request):
    logout(request)
    return redirect('login')
            




@login_required
def dashboard(request):
    return render(request, 'dashboard.html')



@login_required
def apply_leave(request):
    if request.method == 'POST':
        form= Leaveform(request.POST)
        if form.is_valid():
            leave=form.save(commit=False)
            leave.employee=request.user.employee
            leave.save()
            return redirect('my_leaves')        
    else:
        form=Leaveform()

    return render(request,'apply_leave.html',{'form':form})    


@login_required
def my_leaves(request):
    employee= Employee.objects.get(user=request.user)
    leaves=Leave.objects.filter(employee=employee)
    return render(request,'my_leaves.html',{'leaves':leaves})


@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('dashboard')
    employees=Employee.objects.all()
    leaves=Leave.objects.all().order_by('-applied_on')
    return render(request, 'admin_dashboard.html', {'leaves':leaves,'employees':employees})


@login_required
def approve_leave(request,id):
    if not request.user.is_staff:
        return redirect('dashboard')
    leave=Leave.objects.get(id=id)
    leave.status='Approved'
    leave.save()
    return redirect('admin_dashboard')


@login_required
def reject_leave(request,id):
    if not request.user.is_staff:
        return redirect('dashboard')
    leave=Leave.objects.get(id=id)
    leave.status='Rejected'
    leave.save()
    return redirect('admin_dashboard')