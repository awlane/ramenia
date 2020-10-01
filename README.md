# ramenia
Top Ramen group project for U of Memphis Capstone

## Setup notes
The development postgres database should have a db titled ramenia,
with a user named ramenia with password ramen

## Venv setup
Install python3 virtualenv module via some means on your system- this is
not required but will ensure you don't flood your path with unneeded dependencies.
This assumes you're using a Unix OS.

`cd` into the ramenia directory
`python3 -m venv ./venv`
`. ./venv/bin/activate`

To exit the virtual env, use `deactivate`

To enter the virtual env, once again cd to the ramenia directory and run
`. ./venv/bin/activate`

## Install dependencies
`python3 -m pip install Django psycopg2 djangorestframework django-filter Pillow`

## Migrate DB
`python3 manage.py makemigrations rameniaapp`
`python3 manage.py migrate`

## Media
All uploaded media will be put in the django_images folder.