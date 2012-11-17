from django import forms
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import UpdateView

from models import Person, Project, Edition, Role

class Overview(TemplateView):
    template_name = 'people/overview.html'

    def get_context_data(self, **kwargs):
        return {'persons': Person.objects.all().order_by('?')}

class Profile(DetailView):
    template_name = 'people/profile.html'
    model = Person
    context_object_name = 'person'

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
#    form_class =

    context_object_name = 'person'

