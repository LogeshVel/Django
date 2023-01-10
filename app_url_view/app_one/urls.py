from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('<key>/<value>/',views.get_view) # dynamic path variables. this key and value is passed as an argument to the get_view function
]