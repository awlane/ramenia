# ramenia
Top Ramen group project for U of Memphis Capstone

## Docs
- [Developer and maintenance guide](doc/dev-and-maintenance.md)
- [Source code doc](doc/source-code.md)
- [DB Schema](doc/database-schema.svg) (If you have trouble opening this file, try downloading it and opening w/ browser)

## Required Software
Python 3, PostgreSQL

## Setup Notes
The development Postgres database should have a db titled ramenia,
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

## License Notes
Uses the Darkly Bootswatch theme under an MIT license.
Uses icons from game-icons.net for default noodle and profile image under CC.
Uses some icons from https://www.iconfinder.com/iconsets/basic-web-ui-elements under CC-3.0
