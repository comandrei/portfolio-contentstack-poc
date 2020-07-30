from django.urls import path
from .views import homepage, contact, project, projects

urlpatterns = [
    path('contact', contact, name='contact'),
    path('projects', projects, name='projects'),
    path('project/<slug:project_name>', project, name="project_view"),
    path('', homepage, name='home')
]