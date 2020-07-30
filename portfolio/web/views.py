from django.shortcuts import render
# Create your views here.

def homepage(request):
    return render(request, "home.html", {})

def contact(request):
    return render(request, "contact.html", {})

def project(request, project_name):
    return render(request, "project.html", {'project_name': project_name})

def projects(request):
    return render(request, "projects.html", {})