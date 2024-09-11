from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import os

def path_and_rename(instance, filename):
    upload_to = 'face_database'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(timezone.now(), ext)
    return os.path.join(upload_to, filename)

class PersonType(models.Model):
    cat=models.CharField(max_length=255)
    def __str__(self):
        return self.cat

class FaceDB(models.Model):
    image = models.ImageField(upload_to=path_and_rename)
    feature=ArrayField(models.FloatField(),size=128, null=True, blank=True)
    name=models.CharField(max_length=255)
    person_type=models.ForeignKey(PersonType, on_delete=models.CASCADE)
    uniques_id=models.CharField(max_length=255)
    affiliation=models.CharField(max_length=255)
    def __str__(self):
        return self.name
