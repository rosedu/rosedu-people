import factory

from people.models import Role

class RoleFactory(factory.django.DjangoModelFactory):

    FACTORY_FOR = Role

    name = factory.Sequence(lambda n : "admin" + str(n) )




