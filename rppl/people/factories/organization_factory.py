import factory

from people.models import Organization

class OrganizationFactory(factory.django.DjangoModelFactory):

    FACTORY_FOR = Organization

    url = factory.Sequence(lambda n: 'www.rosedu%s.org' % n)

