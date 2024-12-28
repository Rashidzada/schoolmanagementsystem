# School Management System

A comprehensive school management system built with Django, featuring separate interfaces for students, teachers, and administrators.

## Features

- **User Management**
  - Student, Teacher, and Admin roles
  - Secure authentication system
  - Profile management

- **Student Features**
  - View attendance records
  - Check examination results
  - Access class and subject information
  - View announcements

- **Teacher Features**
  - Mark student attendance
  - Upload examination results
  - Manage classes and subjects
  - Post announcements

- **Admin Features**
  - User management
  - Class and section management
  - Subject management
  - System-wide announcements

## Technology Stack

- Python 3.12
- Django 5.1
- Bootstrap 5
- SQLite Database

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Rashidzada/schoolmanagementsystem.git
```

2. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Usage

1. Access the admin interface at `/admin` to set up:
   - Create users (students and teachers)
   - Create classes
   - Create subjects
   - Create student profiles
   - Assign teachers to classes

2. Users can log in at the home page
3. Each user type will be redirected to their respective dashboard

## License

MIT License

## Author

Rashidzada
