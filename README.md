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

