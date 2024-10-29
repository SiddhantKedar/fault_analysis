from django.shortcuts import render, redirect
from django.conf import settings
from .forms import UploadFileForm
import os

def handle_uploaded_file(file):
    # This saves the file in the MEDIA_ROOT directory
    file_path = os.path.join(settings.MEDIA_ROOT, file.name)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def upload_file_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return render(request, 'analysis/success.html')  # After successful upload
    else:
        form = UploadFileForm()
    return render(request, 'analysis/upload.html', {'form': form})
