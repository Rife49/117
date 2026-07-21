from django.contrib import admin
from . import models
from .models import Project,Skill

# Register your models here.
admin.site.register(models.Skill)
admin.site.register(models.Project)
