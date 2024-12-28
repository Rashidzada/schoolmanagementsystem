from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.db.models import Avg

def home(request):
    announcements = Announcement.objects.all().order_by('-date_posted')[:5]
    return render(request, 'core/home.html', {'announcements': announcements})

@login_required
def dashboard(request):
    if request.user.is_student:
        try:
            student = Student.objects.get(user=request.user)
            subjects = student.class_enrolled.subjects.all()
            attendance = Attendance.objects.filter(student=student)
            results = Result.objects.filter(student=student)
            context = {
                'student': student,
                'subjects': subjects,
                'attendance': attendance,
                'results': results
            }
            return render(request, 'core/student_dashboard.html', context)
        except Student.DoesNotExist:
            messages.error(request, 'Student profile not set up. Please contact administrator.')
            return render(request, 'core/profile_incomplete.html')
    
    elif request.user.is_teacher:
        try:
            classes = Class.objects.filter(teacher=request.user)
            subjects = Subject.objects.filter(teacher=request.user)
            context = {
                'classes': classes,
                'subjects': subjects
            }
            return render(request, 'core/teacher_dashboard.html', context)
        except Exception as e:
            messages.error(request, 'Teacher profile not completely set up. Please contact administrator.')
            return render(request, 'core/profile_incomplete.html')
    
    # For admin users or other cases
    return render(request, 'core/admin_dashboard.html')

@login_required
def student_list(request):
    if request.user.is_teacher:
        classes = Class.objects.filter(teacher=request.user)
        students = Student.objects.filter(class_enrolled__in=classes)
        return render(request, 'core/student_list.html', {'students': students})
    return redirect('dashboard')

@login_required
def mark_attendance(request, class_id, subject_id):
    if request.user.is_teacher:
        if request.method == 'POST':
            students = Student.objects.filter(class_enrolled_id=class_id)
            subject = Subject.objects.get(id=subject_id)
            date = request.POST.get('date')
            
            for student in students:
                is_present = request.POST.get(f'student_{student.id}') == 'present'
                Attendance.objects.create(
                    student=student,
                    subject=subject,
                    date=date,
                    is_present=is_present
                )
            messages.success(request, 'Attendance marked successfully!')
            return redirect('dashboard')
        
        students = Student.objects.filter(class_enrolled_id=class_id)
        subject = Subject.objects.get(id=subject_id)
        return render(request, 'core/mark_attendance.html', {
            'students': students,
            'subject': subject
        })
    return redirect('dashboard')

@login_required
def add_result(request, class_id, subject_id):
    if request.user.is_teacher:
        if request.method == 'POST':
            students = Student.objects.filter(class_enrolled_id=class_id)
            subject = Subject.objects.get(id=subject_id)
            exam_type = request.POST.get('exam_type')
            exam_date = request.POST.get('exam_date')
            
            for student in students:
                marks = request.POST.get(f'marks_{student.id}')
                Result.objects.create(
                    student=student,
                    subject=subject,
                    marks=marks,
                    exam_type=exam_type,
                    exam_date=exam_date
                )
            messages.success(request, 'Results added successfully!')
            return redirect('dashboard')
        
        students = Student.objects.filter(class_enrolled_id=class_id)
        subject = Subject.objects.get(id=subject_id)
        return render(request, 'core/add_result.html', {
            'students': students,
            'subject': subject
        })
    return redirect('dashboard')

@login_required
def add_announcement(request):
    if request.user.is_teacher or request.user.is_admin:
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            for_class_id = request.POST.get('for_class')
            
            announcement = Announcement(
                title=title,
                content=content,
                posted_by=request.user
            )
            if for_class_id:
                announcement.for_class_id = for_class_id
            announcement.save()
            
            messages.success(request, 'Announcement posted successfully!')
            return redirect('dashboard')
        
        classes = Class.objects.all()
        return render(request, 'core/add_announcement.html', {'classes': classes})
    return redirect('dashboard')
