# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Projects(models.Model):

    #__Projects_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    startdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    predictedduration = models.IntegerField(null=True, blank=True)

    #__Projects_FIELDS__END

    class Meta:
        verbose_name        = _("Projects")
        verbose_name_plural = _("Projects")


class Task(models.Model):

    #__Task_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    startdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    enddate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Task_FIELDS__END

    class Meta:
        verbose_name        = _("Task")
        verbose_name_plural = _("Task")



#__MODELS__END
