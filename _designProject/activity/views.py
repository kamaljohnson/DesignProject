from django.shortcuts import render
from .forms import ActivityCreationForm


def testingTemplate(request):
    return render(request, 'Testing.html')


def new_activity(request):
    new_activity_form = ActivityCreationForm()
    print('creating form')
    return render(request, 'Activity/new_activity.html', {'form', new_activity_form})
