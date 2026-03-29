from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register,name='register'),
    path('', views.user_login,name='login'),
    path('logout/', views.user_logout,name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('apply-leave/', views.apply_leave, name='apply_leave'),
    path('my-leaves/', views.my_leaves, name='my_leaves'),
    path('admin-dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('approve/<int:id>/', views.approve_leave,name='approve_leave'),
    path('reject/<int:id>/', views.reject_leave,name='reject_leave'),
    path('employee/<int:id>/',views.employee_detail,name='employee_detail')
]
