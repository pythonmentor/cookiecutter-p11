from django.urls import path

from . import views


app_name = "{{ cookiecutter.app_slug }}"

urlpatterns = [
    path("", views.export, name="export")
]
