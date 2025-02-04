from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/', views.student_list, name='student_list'),
    path('mark-attendance/<int:class_id>/<int:subject_id>/', views.mark_attendance, name='mark_attendance'),
    path('add-result/<int:class_id>/<int:subject_id>/', views.add_result, name='add_result'),
    path('add-announcement/', views.add_announcement, name='add_announcement'),
    
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/home.html'), name='logout'),
]
