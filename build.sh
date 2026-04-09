#!/usr/bin/env bash
set -o errexit

python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py shell -c "from django.contrib.auth import get_user_model; import os; User=get_user_model(); username=os.getenv('DJANGO_SUPERUSER_USERNAME'); email=os.getenv('DJANGO_SUPERUSER_EMAIL'); password=os.getenv('DJANGO_SUPERUSER_PASSWORD'); User.objects.filter(username=username).exists() or User.objects.create_superuser(username, email, password)"