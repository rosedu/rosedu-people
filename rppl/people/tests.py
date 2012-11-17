from django.test import TestCase
from models import Person, Project, Edition


class ModelsTest(TestCase):
    def test_person_projects(self):
        p = Person.objects.create(first_name='A', last_name='B')

        proj = Project.objects.create(name='Project')
        edition = Edition.objects.create(project=proj, name='Project, Editia 1')

        edition.add_person(p, 'participant')

        self.assertTrue(p.projects)
