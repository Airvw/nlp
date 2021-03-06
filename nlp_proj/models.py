from django.db import models
# Create your models here.


class Hotel(models.Model):
    def __str__(self):
        return str(self.idx)
    idx = models.IntegerField(default=0)
    text = models.TextField(default='')
    label = models.IntegerField()
    # HotelName = models.TextField()
    # HotelAddress = models.TextField()
    # HotelRating = models.FloatField()
    # ReviewDate = models.DateField()
    # ReviewTitle = models.TextField()
    # ReviewRating = models.FloatField()
    # Positive = models.TextField(default="")
    # Positive = models.TextField(default="")

class UploadFile(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(default="", max_length=15)
    file = models.FileField(upload_to="rawdata")