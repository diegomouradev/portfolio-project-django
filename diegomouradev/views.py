from django.shortcuts import render
from projects.templates import projects_index
def home(request):
    return render(request, 'projects_index.html')