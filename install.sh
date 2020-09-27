#/bin/bash
python3 -m pip install Django psycopg2 djangorestframework django-filter Pillow
python3 manage.py makemigrations rameniaapp
python3 manage.py migrate