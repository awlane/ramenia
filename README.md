# ramenia
Top Ramen group project for U of Memphis Capstone

## Required Software
Python 3, PostgreSQL

## Setup Notes
The development Postgres database should have a db titled ramenia,
with a user named ramenia with password ramen

## Venv Setup
If you're not running this code in a throwaway VM, it is recommended to
use a venv to preserve your Python installation.

Install the python3 virtualenv module via some means on your system

`cd` into the ramenia directory
`python3 -m venv ./venv`
`. ./venv/bin/activate`
`python3 -m pip install Django psycopg2 djangorestframework django-filter Pillow`

To exit the virtual env, use `deactivate`

To enter the virtual env, once again cd to the ramenia directory and run
`. ./venv/bin/activate`

## Install
Run `bash ./install.sh` on any Unix OS or follow along with the commands as necessary.

## User Accounts
Administrator:
admin
password
User 1:
cool_guy
simplepassword
User 2:
cool_girl
simplepassword

## Refresh Development DB
To update your development DB to have the current seed data and all migrations,
run `refresh_db.sb` on any Unix OS or follow along with the commands as necessary.

## Migrate DB
`python3 manage.py makemigrations rameniaapp`
`python3 manage.py migrate`

## Media
All uploaded media will be put in the django_images folder.