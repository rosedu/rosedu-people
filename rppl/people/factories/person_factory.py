import factory

from people.models import Person

class PersonFactory(factory.django.DjangoModelFactory):

    FACTORY_FOR = Person

    username = factory.Sequence(lambda n: "User %d" % n)
    description = factory.Sequence(lambda n: 'My name is %sAndrei%s' % (n, n))
   
    @factory.post_generation
    def organisations(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in.
	    for organisation in extracted:
		self.organisations.add(organisation)  
		
