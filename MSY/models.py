from operator import mod 
from django.db import models
from django.db.models import F 
from django.db.models import Count
import numpy as np
from django.views import *
# Create your models here.

from django.core.validators import FileExtensionValidator

class dataikan(models.Model):
    jenis_usaha    = models.CharField(max_length=50)
    provinsi       = models.CharField(max_length=50)
    jenis_ikan     = models.CharField(max_length=50)
    tahun          = models.FloatField(null=True)
    trip           = models.FloatField(null=True)#trip adalah ton
    ton            = models.FloatField(null=True)#dan ton adalah trip
    def CPUE (self):
        return self.ton/self.trip
    

class UploadedFileJson(models.Model):
    name_suhu = models.CharField(null=True, max_length=100)
    name_krolofil = models.CharField(null=True, max_length=100)
    file_suhu= models.FileField(upload_to='static/json/suhu/',null=True, validators=[FileExtensionValidator(allowed_extensions=['js'])])
    file_krolofil= models.FileField(upload_to='static/json/krolofil/',null=True,validators=[FileExtensionValidator(allowed_extensions=['js'])])
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def save(self, *args, **kwargs):
        self.file_suhu.name = self.name_suhu
        self.file_krolofil.name = self.name_krolofil
        super().save(*args, **kwargs)

class UploadedFileLegenda(models.Model):
    name_suhu = models.CharField(null=True, max_length=100)
    name_krolofil = models.CharField(null=True, max_length=100)
    file_suhu= models.FileField(upload_to='static/legenda/suhu',null=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    file_krolofil= models.FileField(upload_to='static/legenda/krolofil',null=True,validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def save(self, *args, **kwargs):
        self.file_suhu.name = self.name_suhu
        self.file_krolofil.name = self.name_krolofil
        super().save(*args, **kwargs)
