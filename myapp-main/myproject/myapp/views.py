from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import UploadedFile



def upload_file(request):
    if request.method == 'POST' and request.FILES.get('myfile'):
        myfile = request.FILES['myfile']
        uploaded_file = UploadedFile.objects.create(file=myfile)

    files = UploadedFile.objects.all()  # Get all uploaded files
    return render(request, 'upload.html', {'files': files})


def owner_page(request):
    files = UploadedFile.objects.all()  # Fetch all uploaded files
    return render(request, 'owner_page.html', {'files': files})
