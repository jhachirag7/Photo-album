from pydoc import describe
import re
from statistics import mode
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(
        max_length=100, blank=False, null=False)

    def __str__(self):
        return str(self.name)


class Photo(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description
