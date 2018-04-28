# Django: Hello, World!
Create your first Django web application and quickly go through the basics of the open-source python based web framework.
\
\
\
Step 1: Run in the terminal:
```shell
django-admin startproject firstProject
```
\
\
Step 2: Run in the terminal:
```shell
cd firstProject
python3 manage.py migrate
```
This initialises the sqlite3 database.
\
\
\
Step 3: Run in the terminal:
```shell
python3 manage.py runserver
```
This sets up a local server for your web project.  
Open in browser: <http://localhost:8000/>  
If you get a "Congratulations!" page displayed, you're good to proceed.
\
\
\
Step 4: Run in the terminal:
```shell
python3 manage.py startapp firstApp
```
This will initialise an app inside your Django project.  
Include your app in the project by adding the app's name 'firstApp' in INSTALLED_APPS in the project's settings.py file.
\
\
\
Step 5: Include app's urls for project's home page.  
To do this, add the following to urlpatterns in project's urls.py file.
```python
path('home/', include('firstApp.urls'))
```
This will need the include method, so modify the django.urls import in the same file as follows.
```python
from django.urls import path, include
```
\
\
Step 6: Create urls.py inside firstApp with following code.
```python
from django.urls import path
from django.conf.urls import url
from firstApp import views

app_name = 'firstApp'

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
```
This will add the home url for the app.
\
\
\
Step 7: Populate views.py inside the app by adding the following lines:
```python
def home(request):
    return render(request, 'home.html')
```
\
\
Step 8: Create templates folder inside firstApp.  
Then create home.html inside it.  
This html will be displayed as your home page.  
Here's a basic HTML layout.
```html
<DOCTYPE! html>
<html>
    <head>
        <meta charset="utf-8">
        <title>home</title>
    </head>
    <body>
        <h1>
            Hello, World!
        </h1>
    </body>
</html>
```
Run server from manage.py as before and visit <http://localhost:8000/home/>  
You'll see your home.html displayed.  
Note that <http://localhost:8000/> will now show a Page Not Found error.
\
\
\
Step 9: Time to create a model.  
Add the following to models.py inside firstApp.
```python
class Person(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
```
Register this model by adding following lines to admin.py inside firstApp.
```python
from . import models
admin.site.register(models.Person)
```
\
\
Step 10: Register superuser using the following command in terminal:
```shell
python3 manage.py createsuperuser
```
Here for this example, we've used:  
Username: hello  
Email: abc@123.com  
Password: helloworld  
\
\
Software information:  
Ubuntu 16.04 LTS  
Python 3.5.2  
Django 2.0.4