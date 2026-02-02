# Blog Platform (Django REST API)

A simple Blog/Article system built using Django REST Framework with JWT Authentication and role-based access control.

## Features
- User authentication (JWT)
- Roles: Writer, Reader, Admin
- CRUD blog posts
- Comments system
- Pagination & search
- Simple frontend page
- Django Admin panel

## Tech Stack
- Django
- Django REST Framework
- SQLite (can use PostgreSQL)
- HTML + JavaScript frontend

## Setup Instructions
```bash
git clone <repo-url>
cd blog_project
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
