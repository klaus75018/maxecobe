from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)


etude_name_choices = [
    ('Incendie', 'Incendie'),
    ('Décret Tertiaire', 'Décret Tertiaire'),
    ('Autre', 'Autre'),
]

class Etude(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000 ,choices=etude_name_choices)
    thread_id = models.CharField(max_length=1000)
    vs_id = models.CharField(max_length=1000)
    assistant_id = models.CharField(max_length=1000, blank=True, null=True)
    json_db = models.FileField(None, blank=True, null=True)
    json_db_id = models.CharField(max_length=1000, blank=True, null=True)
# Create your models here.
