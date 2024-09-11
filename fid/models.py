from django.db import models
from facedb.models import *
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import os

def path_and_rename(instance, filename):
    upload_to = 'webcam_images'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(timezone.now(), ext)
    return os.path.join(upload_to, filename)

class WebcamImage(models.Model):
    image = models.ImageField(upload_to='webcam_images')
    created_at = models.DateTimeField(auto_now_add=True)

class Attendance(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    query_image=models.ImageField(upload_to=path_and_rename, null=True)
    top1=models.ForeignKey(FaceDB, on_delete=models.CASCADE, related_name='top1')
    top2=models.ForeignKey(FaceDB, on_delete=models.CASCADE, related_name='top2')
    top3=models.ForeignKey(FaceDB, on_delete=models.CASCADE, related_name='top3')
    manual_checkup=models.BooleanField(null=True)
    review=models.BooleanField(null=True)
    def __str__(self):
        return f'1:{self.top1.name}, 2:{self.top2.name}, 3:{self.top3.name}'

    
    
