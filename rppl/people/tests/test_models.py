from django.test import TestCase

from people.factories.organization_factory import OrganizationFactory
from people.models import Organization

from people.factories.project_factory import ProjectFactory
import os.path


class TestOrganization(TestCase):

    def test_create_organization(self):
        """This is an example of how to use Factories. """
        organization_count = Organization.objects.count()

        organization = OrganizationFactory()

        self.assertEqual(organization_count + 1,
                         Organization.objects.count(),
                         "A new organization was not created.")

    def test_get_unicode(self):
        """Testing if the url works"""
        url = "www.rosedu.org"
        organization = OrganizationFactory(url=url)
 
	self.assertEqual(str(organization), url,
                         "Organization conversion to unicode is broken.")
                         

class TestProject(TestCase):
	
	def test_get_logo(self):
		"""Testing if project's url exists"""
		
		project = ProjectFactory()
		logo = project.logo
		
		expected_url = "/resources/upload/" + os.path.basename(logo.url)
		
		self.assertEqual(project.logo_url(), expected_url)
		
		project.logo = None
		
		self.assertEqual(project.logo_url(), 'a',
						"Logo url should be empty if there is no logo.")
		