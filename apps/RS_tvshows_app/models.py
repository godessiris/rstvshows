from __future__ import unicode_literals
from django.db import models


# Create your models here.
class BlogManager(models.Manager):
    def srtv_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) < 5:
            errors["name"] = "Blog name should be at least 5 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Blog description should be at least 10 characters"
        return errors
class Show(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateTimeField()
    network = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Show object: {self.title} {self.network} {self.release_date}>"