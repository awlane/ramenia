#!/bin/bash
# This script is meant to resolve issues in development of swapping between
# branches with heavily different migrations by dropping the tables
# This is mild overkill but was needed to do code review
python3 manage.py flush
echo 'drop owned by ramenia' | python3 manage.py dbshell
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py loaddata dbseed.json