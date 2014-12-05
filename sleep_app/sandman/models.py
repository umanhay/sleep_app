from django.db import models
from django.contrib.auth.models import User

class Mode(models.Model):
    user = models.ForeignKey(User)
    sleep = models.BooleanField()

    def __unicode__(self):
        return self.name


class Contacts(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    charmed = models.BooleanField()

    class Meta:
        verbose_name_plural = "contacts"

    def __unicode__(self):
        return self.name

