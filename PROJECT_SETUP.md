# Project Setup Guide

This guide will help you set up the Django Blog project for development.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git
- A code editor (VS Code, PyCharm, etc.)

## Initial Setup

### 1. Clone the Repository

```bash
git clone https://github.com/NatGok/Blog-using-django.git
cd Blog-using-django
```

### 2. Create Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Django

```bash
pip install django
pip freeze > requirements.txt
```

### 4. Create Django Project

```bash
django-admin startproject blog_project .
```

### 5. Create Django App

```bash
python manage.py startapp blog
```

### 6. Initial Database Migration

```bash
python manage.py migrate
```

### 7. Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 8. Run Development Server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser.

## Project Structure

```
Blog-using-django/
├── .github/
│   └── ISSUE_TEMPLATE/
│       ├── user_story.md
│       └── bug_report.md
├── blog_project/          # Main project directory
│   ├── __init__.py
│   ├── settings.py       # Project settings
│   ├── urls.py           # URL configuration
│   └── wsgi.py           # WSGI configuration
├── blog/                  # Blog app directory
│   ├── migrations/       # Database migrations
│   ├── __init__.py
│   ├── admin.py          # Admin interface
│   ├── apps.py           # App configuration
│   ├── models.py         # Data models
│   ├── tests.py          # Unit tests
│   └── views.py          # View functions
├── templates/             # HTML templates
├── static/                # CSS, JavaScript, images
├── media/                 # User-uploaded files
├── venv/                  # Virtual environment (not in git)
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── README.md              # Project overview
├── USER_STORIES.md        # User stories documentation
├── KANBAN_BOARD.md        # Project board
└── PROJECT_SETUP.md       # This file
```

## Development Workflow

### Creating a New Feature

1. **Check User Stories**: Review [USER_STORIES.md](USER_STORIES.md)
2. **Update Kanban Board**: Move story to "In Progress" in [KANBAN_BOARD.md](KANBAN_BOARD.md)
3. **Create Branch**: `git checkout -b feature/story-name`
4. **Write Tests**: Create tests before implementing the feature
5. **Implement Feature**: Write the code
6. **Run Tests**: `python manage.py test`
7. **Commit Changes**: `git commit -m "Feature: description"`
8. **Push Branch**: `git push origin feature/story-name`
9. **Create Pull Request**: On GitHub
10. **Update Kanban**: Move to "In Review"

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test blog

# Run with verbosity
python manage.py test --verbosity=2

# Keep database after tests
python manage.py test --keepdb
```

### Database Management

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migrations
python manage.py showmigrations

# Revert migration
python manage.py migrate app_name migration_name
```

### Static Files

```bash
# Collect static files for production
python manage.py collectstatic
```

## Configuration

### Environment Variables

Create a `.env` file in the project root (not tracked by git):

```
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Settings for Development

In `blog_project/settings.py`:

```python
# Use environment variables
import os
from pathlib import Path

SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
```

## Common Commands

### Django Admin

```bash
# Create new app
python manage.py startapp app_name

# Create superuser
python manage.py createsuperuser

# Change user password
python manage.py changepassword username

# Shell access
python manage.py shell

# Database shell
python manage.py dbshell
```

### Git Workflow

```bash
# Check status
git status

# Create branch
git checkout -b branch-name

# Stage changes
git add .

# Commit changes
git commit -m "Description"

# Push to remote
git push origin branch-name

# Pull latest changes
git pull origin main
```

## Troubleshooting

### Port Already in Use

```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID [process_id] /F

# macOS/Linux
lsof -ti:8000 | xargs kill -9
```

### Virtual Environment Issues

```bash
# Deactivate current environment
deactivate

# Remove and recreate
rm -rf venv
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Migration Conflicts

```bash
# Reset migrations (WARNING: Development only)
python manage.py migrate app_name zero
rm -rf app_name/migrations/
python manage.py makemigrations app_name
python manage.py migrate
```

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Code Institute Course Materials](https://codeinstitute.net/)
- [Python PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

## Getting Help

- Check [USER_STORIES.md](USER_STORIES.md) for feature requirements
- Review [KANBAN_BOARD.md](KANBAN_BOARD.md) for current progress
- Create an issue using the templates in `.github/ISSUE_TEMPLATE/`
- Consult Django documentation
- Ask in project discussions

## Next Steps

After completing the setup:

1. Review the user stories in [USER_STORIES.md](USER_STORIES.md)
2. Check the kanban board in [KANBAN_BOARD.md](KANBAN_BOARD.md)
3. Start with Sprint 1 stories (Authentication and View Posts)
4. Follow the development workflow above
5. Keep documentation updated as you progress

Happy coding! 🚀
