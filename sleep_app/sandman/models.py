from django.db import models
from django.contrib.auth.models import User

class Mode(models.Model):
    user = models.ForeignKey(User)
    sleep = models.BooleanField()

    def __unicode__(self):
        return self.user

class Contacts(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    charmed = models.BooleanField()

    class Meta:
        verbose_name_plural = "contacts"

    def __unicode__(self):
        return self.name

class Help(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __unicode__(self):
        return self.name



