# List of commands step-by-step

### This project is named `upstore`
---

> Dependancies: `pipenv`

1. `mkdir upstore` - create new directory for the project
2. `cd upstore` - change to the project directory
3. `pipenv install django` - installing `django` in a virtual environment
4. `django-admin startproject upstore .` - start the `upstore project`
5. `python manage.py runserver [port]` - start the server with desired port, if no port is supplied server will start with default port `8000`
6. `python manage.py startapp playground`


## Learnings:

1. In `settings.py`, you can delete the `'django.contrib.sessions'`. We don't use `sessions` now a days