from django import forms
from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import UpdateView

from models import Person, Project, Edition, Role, Link

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



class SForm(forms.ModelForm):

    #link = forms.CharField(max_length=100)
    #    for k,v in args[0].items():
    #        if k.startswith('Q') and k not in self.fields.keys():
    #            self.fields[k] = TestCharField(initial=v, required=True)
    class Meta:
        model = Person
        exclude = ('user',)
    

class ProfileSetup(UpdateView):
    template_name = 'people/profile_set.html'
    model = Person
    form_class = SForm

    form = SForm()
    if form.is_valid():

        form.save()
    context_object_name = 'person'


