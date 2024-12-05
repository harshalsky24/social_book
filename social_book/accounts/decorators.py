from django.shortcuts import redirect
from .models import UploadedFiles

def check_uploaded_files(func):
    def wrapper(request, *args, **kwargs):
        if UploadedFiles.objects.filter(user=request.user).exists():
            return func(request, *args, **kwargs)
        else:
            return redirect('upload_books')  # Redirect to Uploads Books section
    return wrapper
