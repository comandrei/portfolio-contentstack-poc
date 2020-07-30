from django.urls import path
from .views import homepage, contact, project

urlpatterns = [
    path('contact', contact),
    path('project/<slug:project_name>', project),
    path('', homepage)
]