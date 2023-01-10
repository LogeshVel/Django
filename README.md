### Install Django

Windows
```commandline
py -m pip install Django
```

Unix
```commandline
pip install Django
```

### Initialize Django Project

```commandline
django-admin startproject <django_prjt_dir_name>
```

to use current dir as the Django project dir,
```commandline
django-admin startproject .
```

This will create some boilerplate codes.

There will be manage.py file use that to start the dev server 

```commandline
python manage.py runserver
```

### Django app

To create the Django app use the manage.py file that has been created by the Django project initialization.

```commandline
python manage.py startapp <app_name>
```

## Views

#### function based views

```python
# app/views.py
from django.http import HttpResponse
def view_fun(request):
    return HttpResponse("Thanks for View")

# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_fun),
]

# project/urls.py
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls), # domain.com/admin
    path('app/', include('app.urls')) # domain.com/app
]
```

- add the function that takes request as the first parameter and return the HttpResponse (can also return the HTML template)
- in urls.py of the app folder create the urlpatterns list and add the path to the view
- finally, in the urls.py of the project folder include tha path

###### Dynamic view

```python
# app/views.py
from django.http import HttpResponse
def view_fun(request, pathvar1, pathvar2):
    return HttpResponse(f"{pathvar1}:{pathvar2}")

# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<pathvar1>/<pathvar2>', views.view_fun), 
    # the name pathvar1 and pathvar2 must match the parameter of the given function 
    # ex: domain.com/app/pv1/pv2
]

# project/urls.py
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls), # domain.com/admin
    path('app/', include('app.urls')) # domain.com/app
]
```

- add the parameter to that view function
- mention that parameter in the url path in the urlpatterns list

