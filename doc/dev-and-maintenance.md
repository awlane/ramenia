## The complete guide to developing, running, and understanding Ramenia

### Setting up a development environment

In order to actually develop ramenia, you need a development environment.

The recommended install procedure is to clone the repo, create a virtualenv
with python3, and then install dependenies using
`python3 -m pip install Django psycopg2 djangorestframework django-filter Pillow`

You must also have a postgresql database running on your machine with default port. It
should be configured to have a db titled `ramenia`, and a user titled
`ramenia` with the password `ramen`. Obviously, one would not use these credentials
in production but for development it's fine.

Once you have the dependencies and database set up, you need to initialize the
database. This can be done by running `./manage.py migrate`

To run the server, use `./manage.py runserver`. It will start at `localhost:8000`
by default.

### Useful tips in the development environment

The repo contains a set of seed data for development purposes. The easiest way to
load the seed data is to use the `refresh_db.sh` script located in the root of the
repo. This script will completely wipe the database, run all migrations, and
load the example seed data. It is also worth looking inside the `refresh_db.sh`
file for further insight into what it is doing.

When you are finished developing, you may want to add some more seed data. The
easiest way to do this is to run the `dump_data.sh` script which will overwrite
the existing seed data.

The default django admin interface is available at `/admin`

### Learning the codebase

Ramenia is written using Django, a python web framework. It's closest competitor
would be Rails, for comparison. It is highly recommended that you learn the basics
of Django before developing on Ramenia. A good starting tutorial can be found
on the django website located [here](https://www.djangoproject.com/start/).

It is also recommended that you have a good understanding of HTML, CSS, and JS.
Ramenia uses JQuery and AJAX requests in many places.

Given a basic understanding of Django, our project is set up with `ramenia` as our
project name, and `rameniaapp` as our one and only django application. All urls
preceding with `/app` get routed to `rameniaapp`, and `/` redirects to `/app`.

Within rameniaapp, we have also deviated from the standard setup by dividing our
views into separate files. Each file contains 1 or more related views. Look through
them to get a feel for how things are set up. To create a new file, you will need
to add it inside `__init__.py` in the `rameniaapp/views` folder before you can use it
in url routing.

We have also split our models into separate files. Unlike views however, models
need to be added to `rameniaapp/models/models.py` instead of the `__init__.py`.

Once again, it is highly recommended that you look through the code to get a feel
of how things work.

We are also using the Django REST framework in some places. Relevant code for
this can be found in `rameniaapp/serializers.py`. API related views are found
in `rameniaapp/views/rest.py`.

### Architectural overview

The rest of these sections detail how various critical components of the codebase function.

### REST API and other live JS functions

First and foremost, some of this site has live AJAX functionality. This is powered
largely by the functions located in `rameniaapp/views/rest.py`. If you look in the
rameniaapp `urls.py` file, you should see the routes for these functions listed
along with a brief comment about what they do. The easiest way to understand
them is to try querying them in your browser. Some other functions also operate
on simple HTML response codes. For example, following a user returns `200` when
successful.

#### Noodles

Noodles are fairly simple. The noodle model itself contains 2 items of note,
the metadata field and the images. The metadata field is a json document that
contains arbitrary metadata about the noodle. While the site currently enforces
a fairly strict set of data, it was intended to be more flexible. The NoodleImage
model is associated with a Noodle. A noodle can have more than one image, but only
one image should have `main` set to true per noodle.

The noodle page itself has a simple portion where it just displays the information
about the noodle, followed by a set of user actions displayed to logged in users,
and then a reviews section. The reviews section can have a single focused review
or show all reviews. Reviews are loaded with JS after the page is loaded.

#### Lists

Lists are even more simple. It is primarily just a many-to-many relationship between
the `List` model and the `Noodle` model. The list page itself contains little magic
other than some js to allow the delete buttons to work.

#### Search

Search does not have any associated models. The search page allows the user to
query based on the noodle name or the tags. Clicking a tag anywhere on the site
redirects to the search for that tag. Once again, these functions are primarily
powered through code in the `rest.py` file.

#### Moderator tools

TODO
