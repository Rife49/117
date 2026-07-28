from django.shortcuts import render
from . import models 

# Create your views here.
def projects(request):
    projects_list = models.Project.objects.all().order_by('-year')
    context = {'projects': projects_list}
    
    return render(request, 'projects/project_list.html', context)

