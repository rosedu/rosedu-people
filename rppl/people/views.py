from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import UpdateView
from django.core.exceptions import ValidationError

from django.shortcuts import render_to_response
from django.utils.simplejson import dumps

from models import Person, Project, Edition, Role, Link, PersonRole
from random import shuffle

from forms import ProfileSetForm, LinkSetForm, ProjectRoleForm


class Overview(TemplateView):
    template_name = 'people/overview.html'

    def get_context_data(self, **kwargs):
        persons = list(Person.objects.all())
        nr_blanks = 12 - (len(persons) % 12)
        persons += [None] * nr_blanks
        shuffle(persons)
        return {'persons': persons,
                'activities': PersonRole.objects.all().order_by('-timestamp')[:10]
        }

class Profile(DetailView):
    template_name = 'people/profile.html'
    model = Person
    context_object_name = 'person'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)

        roles = sorted(context['person'].person_roles, key=lambda role: role.edition.date_start, reverse=True)
        sorted_roles = []
        while len(roles) > 0:
            sorted_roles += filter(lambda role: role.edition == roles[0].edition, roles)
            roles = filter(lambda role: role.edition != roles[0].edition, roles)

        context['roles'] = sorted_roles

        return context

class Projects(ListView):
    template_name = 'people/projects.html'
    model = Project

class ProjectDetail(DetailView):
    template_name = 'people/project.html'
    model = Project
    context_object_name = 'project'

class ProfileSetup(UpdateView):
    template_name = 'people/profile_set.html'
    model = Person
    context_object_name = 'person'
    success_url = '/'

    def __init__(self, *args, **kwargs):
        super(ProfileSetup, self).__init__(*args, **kwargs)

    def post(self, request, **kwargs):
        person = self.get_object()

        user_data_form = ProfileSetForm(request.POST, instance=person)
        link_form = LinkSetForm(person, request.POST)

        return super(ProfileSetup, self).post(request, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProfileSetup, self).get_context_data(**kwargs)

        person = context['person']

        context['roles'] = dumps(map(str, Role.objects.all()))

        project_editions = {}
        project_id = {}
        for project in Project.objects.all():
            editions = Edition.objects.filter(project=project)
            project_editions[str(project)] = map(str, editions)
            project_id[str(project)] = project.id

        context['project_editions'] = dumps(project_editions)
        context['project_id'] = dumps(project_id)

        context['user_data'] = ProfileSetForm(instance=person)
        context['links'] = LinkSetForm(person)

        projects = Project.objects.all()
        project_forms = [ProjectRoleForm(instance=person, project=p) for p in projects]

        context['project_forms'] = project_forms

        return context



