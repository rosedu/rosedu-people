import factory

from people.factories.project_factory import ProjectFactory
from people.models import Edition
from datetime import datetime, timedelta

class EditionFactory(factory.django.DjangoModelFactory):

	FACTORY_FOR = Edition

	project = factory.SubFactory(ProjectFactory)
	name = factory.Sequence(lambda n: "Edition %d" % n)
	picture = factory.django.ImageField(color='blue')

	date_start = factory.Sequence(lambda n:(datetime.now() + timedelta(days=n)).date(), int)
	date_end = factory.Sequence(lambda n:(datetime.now() + timedelta(days=30 + n)).date(), int)	
	
	@factory.post_generation
	def persons(self, create, extracted, **kwargs):
		if not create:
			# Simple build, do nothing.
			return

		if extracted:
			# A list of groups were passed in.
			for person in extracted:
				self.persons.add(person)