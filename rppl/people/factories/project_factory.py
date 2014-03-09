import factory

from people.models import Project
from factory.django import ImageField

class ProjectFactory(factory.django.DjangoModelFactory):

    FACTORY_FOR = Project
 
    name = factory.Sequence(lambda n: 'name%s' % n)
    url = factory.Sequence(lambda n: 'www.rosedu%s.org' % n)
    description = factory.Sequence(lambda n: 'description%s' % n)
    logo = ImageField()