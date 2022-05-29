from django.shortcuts import render
from django.http import HttpResponse
from face_unlock.project_files.face_unlock import face_recog_start

# Create your views here.


def starting_page(request):
    return render(request, 'face_analyse/index.html')


def index(request):
    face = face_recog_start()
    if face:
        return render(request, 'face_analyse/accessgranted.html')
    else:
        return render(request, 'face_analyse/entrydenied.html')
