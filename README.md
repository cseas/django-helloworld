# Django: Hello, World!
Create your first Django web application and quickly go through the basics of the open-source python based web framework.

Step 1:
Run in the terminal:
```shell
django-admin startproject firstProject
```

Step 2:
Run in the terminal:
```shell
cd firstProject
python3 manage.py migrate
```
This initialises the sqlite3 database.

Step 3:
Run in the terminal:
```shell
python3 manage.py runserver
```
This sets up a local server for your web project.
Open in browser:
[http://localhost:8000/][http://localhost:8000/]
If you get a "Congratulations!" page displayed, you're good to proceed.

Software information:
Ubuntu 16.04 LTS
Python 3.5.2
Django 2.0.4