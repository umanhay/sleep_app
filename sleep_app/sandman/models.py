from django.db import models

class Mode(models.Model):
    #user = models.ForeignKey(user)
    sleep = models.BooleanField()

    def __unicode__(self):
        return self.name


class Contacts(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    charmed = models.BooleanField()

    def __unicode__(self):
        return self.name