from django.db import models
import pyshorteners as pys

# Create your models here.
class UrlToShort(models.Model):
    inputurl = models.TextField(max_length=1000, blank=False)
    outputurl = models.TextField(max_length=500, blank=False)

    def shortenurl(self, inputurl):
        type_tiny = pys.Shortener()
        outputurl = type_tiny.tinyurl.short(inputurl)
        return outputurl

