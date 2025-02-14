from django.urls import path, include

from . import views



urlpatterns = [
    path('incendie/<str:project_name>', views.incendie, name = "incendie"),
    path('DT/<str:project_name>', views.DT, name = "DT"),
    path('dashboard', views.dashboard, name = "dashboard"),
    path('initiate_new_project', views.initiate_new_project, name = "initiate_new_project"),
    path('add_new_project/<str:project_name>', views.add_new_project, name = "add_new_project"),
    path('remarks', views.remarks, name = "remarks"),
]