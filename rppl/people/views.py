from django import forms
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import UpdateView
from django.core.exceptions import ValidationError

from models import Person, Project, Edition, Role, Link
from random import shuffle


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

class Projects(ListView):
    template_name = 'people/projects.html'
    model = Project

class ProjectDetail(DetailView):
    template_name = 'people/project.html'
    model = Project
    context_object_name = 'project'



class SForm(forms.ModelForm):

    person = None
    links = None
    class Meta:
        model = Person
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(SForm, self).__init__(*args, **kwargs)
        if kwargs != {}:
            person = kwargs['instance']
            self.person = Person.objects.get(first_name=person.first_name, last_name=person.last_name)
            links = Link.objects.all().filter(person=self.person)
            self.links = links
            for i in range(6):
                if len(links) > i:
                    self.fields['link' + str(i + 1)] = forms.CharField(max_length=100, initial=links[i])
                else:
                    link = self.fields['link' + str(i + 1)] = forms.CharField(max_length=100, required=False)

    def clean_link1(self):
        self.links.delete()
        if  self.cleaned_data.get('link1', None):
            Link.objects.get_or_create(person = self.person, url = self.cleaned_data.get('link1', None))

    def clean_link2(self):
        if  self.cleaned_data.get('link2', None):
            Link.objects.get_or_create(person = self.person, url = self.cleaned_data.get('link2', None))

    def clean_link3(self):
        if  self.cleaned_data.get('link3', None):
            Link.objects.get_or_create(person = self.person, url = self.cleaned_data.get('link3', None))

    def clean_link4(self):
        if  self.cleaned_data.get('link4', None):
            Link.objects.get_or_create(person = self.person, url = self.cleaned_data.get('link4', None))

    def clean_link5(self):
        if  self.cleaned_data.get('link5', None):
            Link.objects.get_or_create(person = self.person, url = self.cleaned_data.get('link5', None))

    def clean_link6(self):
        if  self.cleaned_data.get('link6', None):
            Link.objects.get_or_create(person = self.person, url = self.cleaned_data.get('link6', None))


    def clean_description(self):
        if len(self.cleaned_data['description'].split(' ')) > 200:
            raise ValidationError("Prea multe cuvinte")

        else:
            return self.cleaned_data['description']

class ProfileSetup(UpdateView):
    template_name = 'people/profile_set.html'
    model = Person
    link = forms.CharField(max_length=100)
    form_class = SForm

    form = SForm()

    if form.is_valid():
        print 'xx'

        form.save()


    context_object_name = 'person'


