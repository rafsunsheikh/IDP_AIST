from django.db import models

class Detection(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to = 'images/')

