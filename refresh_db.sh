#!/bin/bash
python3 manage.py flush
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py loaddata dbseed.json