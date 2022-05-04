import pyshorteners as pys
from .models import UrlToShort

def shortenurl(inputurl):
    type_tiny = pys.Shortener()
    outputurl = type_tiny.tinyurl.short(inputurl)
    return outputurl


def CheckDbOrAdd(inputurl):
    allUrls = UrlToShort.objects.all()
    outputurl = shortenurl(inputurl)
    inDB = False
    notInDB = False
    if len(allUrls) == 0:
        id = len(allUrls) + 1
        UrlToShort(id, inputurl, outputurl).save()
    else:
        while inDB == False and notInDB == False:
            for value in allUrls:
                if value.outputurl == outputurl:
                    inDB = True
                if value.outputurl == allUrls[len(allUrls)-1].outputurl:
                    notInDB = True
        if inDB == False:
            id = len(allUrls) + 1
            UrlToShort(id, inputurl, outputurl).save()
    return outputurl



