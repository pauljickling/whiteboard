# Whiteboard

Whiteboard is a simple interface for answering questions that might be asked in a coding interview during the dreaded whiteboarding section. Whiteboard saves your previous answers so that you can track your progress at answering questions.

At this point in time I don't have an instance of the app available on the internet. This is because the selection of questions I have stored in my database are from *Cracking the Coding Interview*, and using those questions publicly would be a copyright violation. That means as the project currently exists you need to run a copy of the app locally, and then create your own set of questions for the database. The simplest way to do that is to use the Django admin component.

## Installation and Setup

Clone this repository into a directory.

`git clone https://github.com/pauljickling/whiteboard.git`

Next you will want to create your virtual environment for Python:

`virtualenv --python=python3.6 env`

This command creates an environment directory in your project so you can avoid dependencies having conflicting versioning requirements across your local machine. To activate a local env directory run the following:

`source env/bin/activate`

You can use the command `deactivate` to leave that particular virtual environment at any given time.

Finally you need to install the dependencies for Whiteboard (Django and PostgreSQL).

`pip install -r requirements.txt`

To run Whiteboard type the following in the root directory:

`python manage.py runserver`

You can now visit the app at `localhost:8000` in your browser. If you want to make changes to model instances (and you will since initially there will be nothing there!) you will need to create an admin user to use the admin component. You can do so by typing:

`django-admin createsuperuser`

This will prompt you to create a username and password. Be sure to have some method to retrieve it! I've had very annoying instances when I couldn't remember a username and/or password for a Django project I created. Once you have created your username and password you can go to `localhost:8000/admin` to create new problems, or whatever other changes you might want to make.
