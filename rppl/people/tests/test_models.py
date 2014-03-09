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

    def test_get_unicode(self):
	""" Testing if the url works"""
	url = "www.rosedu.org"
	organization = OrganizationFactory(url=url)
 
	self.assertEqual(str(organization),url,
                         "Conversion to unicode is broken.")

