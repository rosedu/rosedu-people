from django.db import models
from django.conf import settings

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    username = models.CharField(max_length=64, default='', blank=True, help_text='Username de pe swarm')
    nickname = models.CharField(max_length=64, default='', blank=True, help_text='IRC nickname')
    email = models.CharField(max_length=100)

    @property
    def name(self):
        return self.first_name + ' ' + self.last_name

    def __unicode__(self):
        return self.name

class Activity(models.Model):
    STATUSES = ((0, 'Active'), (1, 'Suspended'), (2, 'Defunct'))

    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=64)
    status = models.IntegerField(choices=STATUSES, default=0)
    description = models.TextField(max_length=2000, help_text='Markdown text')
    logo = models.ImageField(blank=True, null=True, upload_to=settings.MEDIA_ROOT)

    def is_active(self):
        return self.status == 0

    def __unicode__(self):
        return self.name

class Edition(models.Model):
    activity = models.ForeignKey(Activity)
    title = models.CharField(max_length=100, help_text='Titlu, gen: CDL 2012 primavara')
    description = models.TextField(max_length=2000, help_text='Markdown text, overrides Activity', null=True, blank=True)
    logo = models.ImageField(blank=True, null=True, upload_to=settings.MEDIA_ROOT, help_text='Logo, overrides Activity')
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)

    managers = models.ManyToManyField(Person, related_name='managed')
    helpers = models.ManyToManyField(Person, related_name='helped')

    def get_description(self):
        return self.description or self.activity.description

    def __unicode__(self):
        return self.activity.name + ' ' + self.title

class Project(Activity):
    repo = models.CharField(max_length=100)