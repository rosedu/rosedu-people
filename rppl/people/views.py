from django import forms
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import UpdateView
from django.core.exceptions import ValidationError

from models import Person, Project, Edition, Role, Link, PersonRole
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



class SForm(forms.ModelForm):

    person = None
    links = None

    max_links = 6

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

            for i in xrange(self.max_links):
                if len(links) > i:
                    self.fields['link%d' % (i + 1)] = forms.CharField(max_length=100, initial = links[i], required = False)
                else:
                    self.fields['link%d' % (i + 1)] = forms.CharField(max_length=100, required = False)


            #Add forms for project roles
            roles = [(r, r) for r in Role.objects.all()]

            person_roles = self.person.person_roles
            for project in Project.objects.all():
                index = 0

                #Get project roles for the current project
                project_roles = filter(lambda role: role.edition.project == project, person_roles)

                #Add inputs for all roles
                for role in project_roles:
                    edition_choices = [(e, e) for e in Edition.objects.filter(project=project)]
                    self.fields['%sedition%d' % (project, index)] = forms.ChoiceField(choices = edition_choices,
                                                                                      initial = role.edition,
                                                                                      label = project)
                    self.fields['%srole%d' % (project, index)] = forms.ChoiceField(choices = roles,
                                                                                   initial = role.role,
                                                                                   label = project)
                    index += 1


    def clean(self):
        self.links.delete()
        for i in xrange(self.max_links):
            link = self.cleaned_data.get('link%d' % i, None)
            if link:
                Link.objects.get_or_create(person = self.person, url = link)

        if len(self.cleaned_data['description'].split(' ')) > 200:
            raise ValidationError("Too many words")
        else:
            return self.cleaned_data

class ProfileSetup(UpdateView):
    template_name = 'people/profile_set.html'
    model = Person
    form_class = SForm

    form = SForm()

    if form.is_valid():
        form.save()


    context_object_name = 'person'


