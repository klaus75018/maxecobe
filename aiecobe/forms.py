from django import forms
from django.forms import ModelChoiceField


class NewProjectForm(forms.Form):

    project_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    study_type = forms.ChoiceField(choices=[('Incendie', 'Incendie'), ('Décret Tertiaire', 'Décret Tertiaire'), ('Autre', 'Autre')])

class AddNewProjectForm(forms.Form):

    study_type = forms.ChoiceField(choices=[('Incendie', 'Incendie'), ('Décret Tertiaire', 'Décret Tertiaire'), ('Autre', 'Autre')])
    