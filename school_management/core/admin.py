from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Class, Student, Subject, Attendance, Result, Announcement

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_student', 'is_teacher', 'is_admin')
    list_filter = ('is_student', 'is_teacher', 'is_admin')
    fieldsets = UserAdmin.fieldsets + (
        ('User Type', {'fields': ('is_student', 'is_teacher', 'is_admin')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(Result)
admin.site.register(Announcement)
