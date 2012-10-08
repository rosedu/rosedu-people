from django.db import models
from django.conf import settings

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    username = models.CharField(max_length=64, default='', blank=True, help_text='Username de pe swarm')
    nickname = models.CharField(max_length=64, default='', blank=True, help_text='IRC nickname')
    email = models.CharField(max_length=100)

    class Meta:
        unique_together = ('first_name', 'last_name')

    @property
    def name(self):
        return self.first_name + ' ' + self.last_name

    def __unicode__(self):
        return self.name

class Activity(models.Model):
    STATUSES = ((0, 'Active'), (1, 'Suspended'), (2, 'Defunct'))

    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=64, blank=True, default='')
    status = models.IntegerField(choices=STATUSES, default=0)
    description = models.TextField(max_length=2000, help_text='Markdown text')
    logo = models.ImageField(blank=True, null=True, upload_to=settings.MEDIA_ROOT)

    def is_active(self):
        return self.status == 0

    @property
    def editions(self):
        return self.edition_set.order_by('-date_start')

    def __unicode__(self):
        return self.name

class Event(Activity):
    """ Public event
    """
    location = models.CharField(max_length=100, blank=True, null=True)

class Project(Activity):
    """ Software project.
    """
    repo = models.CharField(max_length=100, blank=True, null=True)

class Version(models.Model):
    project = models.ForeignKey(Activity)
    repo = models.CharField(max_length=100, blank=True, default='')
    version = models.CharField(max_length=100, help_text='Numele versiunii')

    managers = models.ManyToManyField(Person, related_name='projectmanaged', null=True, blank=True)
    developers = models.ManyToManyField(Person, related_name='developed', null=True, blank=True)

    def __unicode__(self):
        return self.version

class Edition(models.Model):
    event = models.ForeignKey(Activity)
    title = models.CharField(max_length=100, help_text='Titlu, gen: CDL 2012 primavara')
    description = models.TextField(max_length=2000, help_text='Markdown text, overrides Activity', null=True, blank=True)
    logo = models.ImageField(blank=True, null=True, upload_to=settings.MEDIA_ROOT, help_text='Logo, overrides Activity')
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)

    managers = models.ManyToManyField(Person, related_name='managed', null=True, blank=True)
    helpers = models.ManyToManyField(Person, related_name='helped', null=True, blank=True)

    def get_description(self):
        return self.description or self.event.description

    def __unicode__(self):
        return self.title
