from django.shortcuts import render
# Create your views here.

def testingTemplate(request):
    return render(request, 'Testing.html')
