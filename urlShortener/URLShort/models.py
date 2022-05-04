from django.db import models

# Create your models here.
class UrlToShort(models.Model):
    inputurl = models.TextField(max_length=1000, blank=False)
    outputurl = models.TextField(max_length=500, blank=False)




