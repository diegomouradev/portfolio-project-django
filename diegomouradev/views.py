from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Projects


def home(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'home.html', context)
