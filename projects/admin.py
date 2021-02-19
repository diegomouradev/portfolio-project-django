from django.contrib import admin

# Register your models here.
from projects.models import Projects


class ProjectsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Projects, ProjectsAdmin)
