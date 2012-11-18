from django.test import TestCase
from models import Person, Project, Edition, Role, PersonRole


class ModelsTest(TestCase):
    def test_person_projects(self):
        p = Person.objects.create(first_name='A', last_name='B')

        proj = Project.objects.create(name='Project')
        edition = Edition.objects.create(project=proj, name='Project, Editia 1')

        edition.add_person(p, 'participant')

        self.assertTrue(p.projects)

        # Test that a new role is being created on the fly when appropriate
        role_count_before = Role.objects.count()

        edition.add_person(p, 'xyz_nonsense')

        role_count_after = Role.objects.count()

        self.assertEqual(role_count_after, role_count_before + 1)

        # Test that a combination person-role can only exist once in PersonRole
        other_person = Person.objects.create(first_name='ABC', last_name='XYZ')

        person_role_count_before = PersonRole.objects.count()

        edition.add_person(other_person, 'participant')

        person_role_count_after_adding_a_person_once = PersonRole.objects.count()

        edition.add_person(other_person, 'participant')

        person_role_count_after_adding_a_person_twice = PersonRole.objects.count()

        self.assertEqual(person_role_count_after_adding_a_person_once, person_role_count_before + 1)
        self.assertEqual(person_role_count_after_adding_a_person_twice, person_role_count_before + 1)

