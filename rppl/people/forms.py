from django import forms
from models import Person, Project, Edition, Role, Link, PersonRole
from django.core.exceptions import ValidationError

class ProjectRoleWidget(forms.MultiWidget):
    def __init__(self, editions, roles, *args, **kwargs):
        widgets = (
            forms.Select(choices = [(e, e) for e in editions]),
            forms.Select(choices = [(r, r) for r in roles])
        )
        super(ProjectRoleWidget, self).__init__(widgets, *args, **kwargs)

    def decompress(self, value):
        if value:
            return value.split('|')
        return ['', '']

class ProjectRoleField(forms.MultiValueField):
    def __init__(self, editions, roles, *args, **kwargs):
        self.widget = ProjectRoleWidget(editions, roles)
        fields = (
            forms.ChoiceField(choices=[(e, e) for e in editions]),
            forms.ChoiceField(choices=[(r, r) for r in roles])
        )
        super(ProjectRoleField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return '|'.join(data_list)
        return None

class LinkSetForm(forms.Form):
    person = None

    max_links = 6

    def __init__(self, *args, **kwargs):
        self.person = kwargs.pop('instance')
        super(LinkSetForm, self).__init__(*args, **kwargs)

        if len(args) > 0 and args[0] is not None:
            self.get_extra(args[0])
            return

        links = Link.objects.filter(person=self.person)

        for i in xrange(len(links)):
            self.fields['link%d' % (i + 1)] = forms.CharField(
                    max_length=100,
                    initial = links[i],
                    required = False)

    def get_extra(self, post):
        if post is None:
            return
        field_names = post.keys()
        for f in field_names:
            if f.startswith('link'):
                self.fields[f] = forms.CharField(max_length=100, required=False)

    def clean(self):
        # Delete empty entries.
        for key, value in self.cleaned_data.items():
            if not value:
                del self.cleaned_data[key]
        return self.cleaned_data

    def save(self):
        # Delete filters not present in cleared data.
        # Use the fact that the QuerySet is lazy.
        removed_links = Link.objects.filter(person=self.person)
        links = self.cleaned_data.values()
        for l in links:
            removed_links = removed_links.exclude(url=l)

        # Delete links that are not present in cleaned data.
        removed_links.delete()

        for l in links:
            Link.objects.get_or_create(url=l, person=self.person)

class ProjectRoleForm(forms.Form):
    person = None
    project = None

    def __init__(self, *args, **kwargs):
        self.person = kwargs.pop('instance')
        self.project = kwargs.pop('project')

        super(ProjectRoleForm, self).__init__(*args, **kwargs)

        if len(args) > 0 and args[0] is not None:
            self.get_extra(args[0])
            return

        roles = Role.objects.all()
        editions = Edition.objects.filter(project=self.project)

        person_roles = filter(lambda role: role.edition.project == self.project, self.person.person_roles)

        for i in xrange(len(person_roles)):
            role = person_roles[i]
            field = ProjectRoleField(
                    editions, roles,
                    initial = '|'.join([str(role.edition), str(role.role)]))

            self.fields['%d_role%d' % (self.project.id, i)] = field

    def get_extra(self, post):
        if post is None:
            return
        field_names = post.keys()

        roles = Role.objects.all()
        editions = Edition.objects.filter(project=self.project)

        for f in field_names:
            if f.startswith('%d_role' % self.project.id):
                # Truncate the name so the field is correctly named
                self.fields[f[:-2]] = ProjectRoleField(editions, roles)

    def save(self):
        entries = [e.split('|') for e in self.cleaned_data.values()]

        editions = {}
        roles = {}

        for e in Edition.objects.filter(project=self.project):
            editions[e.name] = e

        for r in Role.objects.all():
            roles[r.name] = r

        removed_entries = PersonRole.objects.filter(person=self.person, edition__project=self.project)
        for e, r in entries:
            removed_entries = removed_entries.exclude(edition=editions[e], role=roles[r])

        print "remove", removed_entries
        removed_entries.delete()

        print "add", entries

        for e, r in entries:
            PersonRole.objects.get_or_create(person=self.person, edition=editions[e], role=roles[r])


class ProfileSetForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ('user', 'organisations')

    def clean(self):
        if len(self.cleaned_data['description'].split(' ')) > 200:
            raise ValidationError("Too many words")
        else:
            return self.cleaned_data


