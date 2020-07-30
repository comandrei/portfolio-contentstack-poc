from django.shortcuts import render
from django.urls import reverse
from .cs import ContentStackAPIWrapper

def _generate_project_thumbnail(project):
    curated_project = {
            'title': project['title'],
            'url': reverse('project_view', args=(project['uid'], )),
            'external_url': project['url']['href'],
            'description': project['project_description']
    }
    for media_item in project['media']:
        if 'screenshot' in media_item:
            curated_project['image'] = media_item['screenshot']['image']['url']
        if 'video' in media_item:
            curated_project['video'] = media_item['video']['video']['url']
    return curated_project

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
    cs = ContentStackAPIWrapper()
    project = cs.get_entry('project', project_name)
    curated_project = _generate_project_thumbnail(project)
    return render(request, "project.html", {'project': curated_project})

def projects(request):
    cs = ContentStackAPIWrapper()
    projects = cs.get_multiple_entries('project')
    featured_projects = []
    for project in projects['entries']:
        curated_project = _generate_project_thumbnail(project)
        featured_projects.append(curated_project)

    return render(request, "projects.html", {'featured_projects': featured_projects})