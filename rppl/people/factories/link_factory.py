import factory

from people.factories.person_factory import PersonFactory
from people.models import Link

class LinkFactory(factory.django.DjangoModelFactory):
	
    FACTORY_FOR = Link

    url = factory.Sequence(lambda n: 'www.rosedu%s.org' % n)

    person = factory.SubFactory(PersonFactory)
