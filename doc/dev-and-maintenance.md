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

Moderator tools are accessible to users in the moderator group, which they are currently automatically added to if they stay above 1000 rep and removed from if they go below that (our example user cool_girl has a rep above that to prevent issues from demonstrating the moderator granting ActionHook). We will likely want more fine grained permissions in the future- the current non-moderator/moderator distinction is a bit too simplified for more than a proof of concept but this code can easily be expanded or modified as the case may be. Groups are added via the `admin` page from the website.

##### Edits

`Edits` (in Ramenia) are a generic model name used to refer to the creation or alteration of a noodle object, as these share a lot of the same code and it was felt to be more clean to handle them this way. 
`Edit` objects are created through the forms on the Add and Edit Ramen pages, which populate the `change` field with a JSON description of the fields of the noodle. This was originally meant to allow for more flexibility as previously mentioned but time constraints, validation, and providing diff functionality made this difficult.
Once an edit is created through this form, it must be approved by a moderator to be applied, which is done through the view at `app/mod/edits` by pressing the Approve button. The Reject button will delete the edit, as we assume a rejected edit is not worth keeping- this may make more sense in the future. 

The current functionality for processing and applying edits is contained in `views/edit_utils.py` to make these functions more reusable and fixable. As currently implemented, this functionality is invoked from its `apply_edit()` function, which has none of the functional logic other than assuming edits have a `noodle` and `image` field. This function currently handles creating and editing ramen, adding images and removing defaults if an alternative is provided, and updating tags. We additionally have functionality for setting a main image (will be displayed first in carousel) and removing images, but these (while tested to be working during development) were not implemented into the GUI in time.

#### Reports

`Reports` are actually effectively split into model classes referencing Noodles, Reviews, and Profiles. This is due to Django not providing polymorphic interfaces, which complicated our schema. `Reports` just consist of a reasoning, status, reporter, and object (the type of which is respective to its class). These reports are viewed from separate views linked from the mod page for each type to simplify the queries, as we would need to cast every single report to be its correct type every time otherwise (this is an area which can be improved in the future). There are four implemented actions for reports at the moment: changing status, banning the responsible user, ignoring the report (deletes report), and deleting the offending content (which removes all related reports as well).
Changing status as implemented is currently used to switch a report from its default "open" state to "resolved" (such as a noodle that was vandalized but was edited and fixed) or "spam" (a fake submission meant to annoy moderators or harass someone), which is simply done by changing the interior field through the provided buttons or `update_report_status` method.
Banning the user deletes the user's account, profile, and reviews but not their noodles- this means that occasionally you have noodles without an editor or reports without a reporter, which needs to be handled in the code.
Deleting content means simply deleting the reported object, except for profiles. As profiles are expected to be 1:1 to users, we instead change all user modifiable fields to something inoffensive if it makes sense versus banning a user.
