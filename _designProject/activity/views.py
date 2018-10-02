from django.http import HttpResponse
from django.shortcuts import render
from .forms import ActivityCreationForm
from .models import Activity
from django.template import loader

def testingTemplate(request):
    return render(request, 'Testing.html')


def new_activity(request):
    new_activity_form = ActivityCreationForm()
    return render(request, 'Activity/new_activity.html', {'form': new_activity_form})


def all_activities(request):
    all_activities = Activity.objects.all()
    context = {'all_activities': all_activities}
    template = loader.get_template('Activity/my_activities.html')

    return HttpResponse(template.render(context, request))
