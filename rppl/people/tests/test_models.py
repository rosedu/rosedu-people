from django.test import TestCase

from people.factories.organization_factory import OrganizationFactory
from people.models import Organization

class TestOrganization(TestCase):

    def test_create_organization(self):
        """ This is an example of how to use Factories. """
        organization_count = Organization.objects.count()

        organization = OrganizationFactory()

        self.assertEqual(organization_count + 1,
                         Organization.objects.count(),
                         "A new organization was not created.")

