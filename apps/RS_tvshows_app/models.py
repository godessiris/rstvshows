from __future__ import unicode_literals
from django.db import models




# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        
        if len(postData['title']) == 0:
            errors["title"] = "Please enter a Show title!"
        if len(postData['description']) < 5:
            errors["description"] = "Please, Describe the show with more than 5 words!!"
        if len(postData['network']) == 0:
            errors["network"] = "Please enter a network"
        if len(postData['release_date']) < 10:
            errors["release_date"] = "Dont forget the date and it should be mm/dd/yyyy!"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateTimeField()
    network = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=ShowManager()

    def __repr__(self):
        return f"<Show object: {self.title} {self.network} {self.release_date}>"