#!/bin/sh
cd /code
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --no-input
django-admin compilemessages
python manage.py runserver 0.0.0.0:8000
