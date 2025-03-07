#!/bin/bash

# Navigate to the Django project directory
cd /Users/amit/Projects/Django/Github-repo-management-backend

# Remove all migration files
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

# Make new migrations and migrate
python manage.py makemigrations
python manage.py migrate

echo "Migrations have been reset."