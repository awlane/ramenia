#!/bin/bash
python3 manage.py flush
echo 'drop owned by ramenia' | python3 manage.py dbshell
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py loaddata dbseed.json