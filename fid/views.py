from django.shortcuts import render
import base64
import os
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import WebcamImage
from datetime import datetime
import face_recognition
from fid.models import Attendance
from facedb.models import FaceDB

def index(request):
    return render(request, 'fid/index.html')

def upload_image(request):
    print('1')
    if request.method == 'POST':
        image_data = request.POST.get('image_data')
        print('2')
        # Convert the base64-encoded image data to a binary format
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
        format, imgstr = image_data.split(';base64,') 
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name=f'{timestamp}.{ext}')

        # Generate a timestamp to use as the filename

        webcam_image = WebcamImage(image=data)
        webcam_image.save()
        print('3', webcam_image.image.path)
        image = face_recognition.load_image_file(webcam_image.image.path)
        face_encoding = face_recognition.face_encodings(image)[0]
        '''
        query_image=models.ImageField(upload_to=path_and_rename, null=True)
        top1=models.ForeignKey(FaceDB, on_delete=models.CASCADE, related_name='top1')
        top2=models.ForeignKey(FaceDB, on_delete=models.CASCADE, related_name='top2')
        top3=models.ForeignKey(FaceDB, on_delete=models.CASCADE, related_name='top3')
        manual_checkup=models.BooleanField(null=True)
        review=models.BooleanField(null=True)
        '''
        #Steps
        #1. Extract feature of webcam image face_recognition
        #2. get top3 results from database
        print(face_encoding)
        queryset = FaceDB.objects.raw('select t1.id from facedb_facedb as t1 order by cube_distance(cube(%s), cube(t1.feature)) limit 3' , [list(face_encoding)])
        #queryset = FaceDB.objects.raw('select cube(%s)' , [list(face_encoding)])
        print(queryset)

        attandance = Attendance(query_image=data, top1=queryset[0], top2=queryset[1], top3=queryset[2])
        attandance.save()
        #3. create attandance object and save
        # Generate a timestamp to use as the filename

        return JsonResponse({'status': 'success', 'message': 'Attandance marked successfully'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

