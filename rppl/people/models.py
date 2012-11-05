from django.db import models
from django.conf import settings

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.CharField(max_length=100)

    description = models.CharField(max_length=200)

    class Meta:
        unique_together = ('first_name', 'last_name')

    @property
    def name(self):
        return self.first_name + ' ' + self.last_name

    def __unicode__(self):
        return self.name

class Link(models.Model):
    """ Link for person's external accounts """
    url = models.CharField(max_length=100)
    person = models.ForeignKey(Person)

class Organization(models.Model):
    """ External affiliations for users """
    url = models.CharField(max_length=100)
    persons = models.ManyToManyField(Person)

class Project(models.Model):
    """ Project in community """
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    logo = models.ImageField(blank=True, null=True, upload_to=settings.MEDIA_ROOT)

class Edition(models.Model):
    """ Project edition """
    project = models.ForeignKey(Project)
    picture = models.ImageField(blank=True, null=True, upload_to=settings.MEDIA_ROOT)
    name = models.CharField(max_length=100)

class Role(models.Model):
    """ A role that can be given to many persons in an editition """
    name = models.CharField(max_length=100)

    edition = models.ForeignKey(Edition)
    persons = models.ManyToManyField(Person)
