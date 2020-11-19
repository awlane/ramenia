#/bin/bash
# Script for fresh installs, will install Python modules and set up DB
python3 -m pip install Django psycopg2 djangorestframework django-filter Pillow
python3 manage.py migrate
python3 manage.py loaddata dbseed.json