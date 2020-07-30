from django.shortcuts import render
from django.urls import reverse
from .cs import ContentStackAPIWrapper

def _generate_project_thumbnail(project):
    return  {
            'title': project['title'],
            'image': project['media'][0]['screenshot']['image']['url'] if project['media'][0]['screenshot']['image'] else '', 
            'url': reverse('project_view', args=(project['uid'], ))
    }
def homepage(request):
    cs = ContentStackAPIWrapper()
    page = cs.get_homepage()
    featured_projects = []
    for project in page['featured_projects']:
        proj = cs.get_entry(project['_content_type_uid'], project['uid'])
        curated_project = _generate_project_thumbnail(proj)
        featured_projects.append(curated_project)

    return render(request, "home.html", {'page': page, 'featured_projects': featured_projects})

def contact(request):
    return render(request, "contact.html", {})

def project(request, project_name):
    return render(request, "project.html", {'project_name': project_name})

def projects(request):
    cs = ContentStackAPIWrapper()
    projects = cs.get_multiple_entries('project')
    featured_projects = []
    print(projects)
    for project in projects['entries']:
        curated_project = _generate_project_thumbnail(project)
        featured_projects.append(curated_project)

    return render(request, "projects.html", {'featured_projects': featured_projects})