from django import forms
from .models import Activity, Idea, Project, Tag


class ActivityCreationForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('name', 'tags')
