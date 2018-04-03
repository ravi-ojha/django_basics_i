# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Question(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question)
    description = models.TextField()
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(default=timezone.now)
