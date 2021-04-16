from django.db import models

class Detection(models.Model):
    name = models.CharField(max_length=50)
    detection_date = models.DateField(auto_now_add=True, blank=True)
    detection_time = models.TimeField(auto_now_add=True, blank=True)
    # models.TimeField(auto_now=False, auto_now_add=False, **options)
    image = models.FileField(upload_to = 'images/')


class Tower(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    