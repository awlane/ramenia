## Technical Specifications Guide

### Architecture
This project runs off the Django web framework, which is an MVC-type framework (Django uses Model-Template-View as their terminology instead). Django provides session handling, a web server, and a database API. Django is run with the Python 3.8.5 interpreter. The front end uses web technologies and is rendered through the web browser.

#### Frontend
The front end is HTML and JQuery code dynamically generated from the templates by Django, with CSS styling via Bootstrap's preconfigured stylesheets. When run locally, the site uses port 8000 by default, and can be accessed by simply using the URL `localhost:8000`.

#### Backend
##### Framework
This project was built with Django version 3.1.1 and patches for major overhauls or changes should be made with this in mind.
##### Server
We use the default WSGI server provided by Django, which is effectively just a translator between client HTTP requests and Python. An automatic configuration for testing is created through the `manage.py startproject`, any alterations to which are viewable in `ramenia/settings.py`
WSGI runs on port 8000 for development applications by default.
##### Database
We use PostgreSQL running locally for our database due to native JSON support. Access to the database is configured via a superuser account named ramenia which must be preconfigured to allow Django to have DB access. A table called ramenia is similarly expected.
PostgresQL runs on port 5432.