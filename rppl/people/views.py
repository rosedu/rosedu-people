from random import shuffle

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.utils.simplejson import dumps
from django.utils.decorators import method_decorator
from django.views.generic import (TemplateView, DetailView, ListView,
                                  FormView)
from django.views.generic.edit import UpdateView


from decorators import same_user_from_request_required
from forms import (ProfileSetForm, LinkSetForm, ProjectRoleForm,
                   ProfileCreateForm)
from models import Person, Project, Edition, Role, PersonRole
from braces.views import LoginRequiredMixin


class Overview(LoginRequiredMixin,
               TemplateView):
    NO_ACTIVITIES = 10
    GRID_LINE = 12
    template_name = 'people/overview.html'

    def get_context_data(self, **kwargs):
        persons = list(Person.objects.all())
        nr_blanks = self.GRID_LINE - (len(persons) % self.GRID_LINE)
        persons += [None] * nr_blanks
        shuffle(persons)
        return {'persons': persons,
                'activities': PersonRole.objects.all().order_by('-timestamp')[:self.NO_ACTIVITIES]
        }


class Profile(LoginRequiredMixin,
              DetailView):

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


class Projects(LoginRequiredMixin,
               ListView):

    permission_required = "elsgg.view_wholesale"
    template_name = 'people/projects.html'
    model = Project


class ProjectDetail(LoginRequiredMixin,
                    DetailView):

    template_name = 'people/project.html'
    model = Project
    context_object_name = 'project'


class ProfileCreate(LoginRequiredMixin,
                    FormView):

    template_name = 'people/profile_create.html'
    form_class = ProfileCreateForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password2']
            user = form.save()
            username = user.username
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile', user.pk)
        return render(request, self.template_name, {'form': form})


class ProfileSetup(LoginRequiredMixin,
                   UpdateView):

    template_name = 'people/profile_set.html'
    model = Person
    context_object_name = 'person'
    success_url = '/'

    @method_decorator(same_user_from_request_required)
    def dispatch(self, *args, **kwargs):
        """Decorated for authorization and authentication"""
        return super(ProfileSetup, self).dispatch(*args, **kwargs)

    def post(self, request, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(**kwargs)

        # Get forms from POST data.

        person = context['person']
        all_forms = [context['user_data'], context['links']]
        # Ugly hack to allow only staff to edit projects
        if person.is_staff:
            all_forms += context['project_forms']

        # Check if at least one is invalid.
        valid_results = [f.is_valid() for f in all_forms]
        if False in valid_results:
            return self.render_to_response(context)
        else:
            for f in all_forms:
                f.save()

        # Redirect to user profile.
        return redirect('profile', self.object.pk)

    def get_context_data(self, **kwargs):
        context = super(ProfileSetup, self).get_context_data(**kwargs)

        data = self.request.POST if self.request.method == 'POST' else None

        person = context['person']
        project_editions = {}
        project_id = {}
        for project in Project.objects.all():
            editions = Edition.objects.filter(project=project)
            project_editions[str(project)] = map(str, editions)
            project_id[str(project)] = project.id

        context['roles'] = dumps(map(str, Role.objects.all()))
        context['project_editions'] = dumps(project_editions)
        context['project_id'] = dumps(project_id)

        context['user_data'] = ProfileSetForm(data, instance=person)
        context['links'] = LinkSetForm(data, instance=person)
        context['project_forms'] = [ProjectRoleForm(data, instance=person, project=p) for p in Project.objects.all()]

        return context
