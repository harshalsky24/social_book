from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.conf import settings
# Create your models here.

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    public_visibility = models.BooleanField(default=True)
    birth_year = models.PositiveBigIntegerField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)

    @property
    def age(self):
        if self.birth_year:
            return date.today.year - self.birth_year
        return None
    
class UploadedFiles(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="uploaded_files")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    Visibility = models.BooleanField(default=True)
    file = models.FileField(upload_to='upload_files/', null=False, blank=False)
    cost = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    year_of_published = models.PositiveBigIntegerField(null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title