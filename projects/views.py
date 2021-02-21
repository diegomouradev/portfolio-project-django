from django.shortcuts import render
from django.views import generic
from projects.models import Projects
# Create your views here.


def projects_index(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/projects_index.html', context)


def project_detail(request, pk):
    project = Projects.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/project_detail.html', context)
