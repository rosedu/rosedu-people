from django.views.generic import TemplateView, DetailView, ListView

from models import Person, Activity, Edition

class Overview(TemplateView):
    template_name = 'people/overview.html'

    def get_context_data(self, **kwargs):
        return {'persons': Person.objects.all()}

class Profile(DetailView):
    template_name = 'people/profile.html'
    model = Person
    context_object_name = 'person'

class Activities(ListView):
    template_name = 'people/activities.html'
    model = Activity

class ActivityDetail(DetailView):
    template_name = 'people/activity.html'
    model = Activity
    context_object_name = 'activity'

class EditionDetail(DetailView):
    template_name = 'people/edition.html'
    model = Edition
    context_object_name = 'edition'

