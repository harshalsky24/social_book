from rest_framework import serializers
from .models import UploadedFiles

class UplodedFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFiles
        fields = ['id', 'title', 'description', 'file','Visibility', 'cost', 'year_of_published']
