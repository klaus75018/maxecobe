from django.urls import path, include

from . import views



urlpatterns = [
    path('index', views.index, name = "index"),
    path('contact_main', views.contact_main, name = "contact_main"),
]