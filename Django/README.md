## Django REST API CRUD Tutorial
A repository that helps to kickstart [Django framework](https://www.djangoproject.com/) is a powerful and flexible toolkit for building Web applications.

## Requirements
- Python 3.10.0
- Django 4.1.2

## Features

- Create Movie
- List Movies
- Update Movie
- Delete Movie


## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```
## Running the Application

Create the DB tables first:
```
python manage.py makemigrations
python manage.py migrate
```
Run the development web server:
```
python manage.py runserver 

## Get List of Movies

hen you can add new movie, update existing one and also can delete.