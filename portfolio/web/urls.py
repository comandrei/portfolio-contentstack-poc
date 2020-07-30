from django.urls import path
from .views import homepage, contact, project

urlpatterns = [
    path('contact', contact, name='contact'),
    path('projects', project, name='projects'),
    path('project/<slug:project_name>', project),
    path('', homepage, name='home')
]