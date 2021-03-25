from django.contrib import admin
from .models import Hotel
from .models import UploadFile

# Register your models here.
admin.site.register(Hotel)
admin.site.register(UploadFile)