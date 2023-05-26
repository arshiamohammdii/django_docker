from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shorten/", views.url_shortener, name="url_shortener_api")
]

