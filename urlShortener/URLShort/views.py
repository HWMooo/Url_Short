from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import UrlToShort
from .functions import shortenurl


# Create your views here.

def Home(request):
    return render(request, 'base.html')

@csrf_exempt
def Shorten(request):
    if request.method == 'POST':
        inputurl = request.POST.get('inputurl')
        outputurl = shortenurl(inputurl)
        allUrls = UrlToShort.objects.all()
        print("here is all instances of UrlToShort", allUrls)
        id = len(allUrls) + 1
        UrlToShort(id, inputurl, outputurl).save()
        urloutput = {'output': outputurl}
        return render(request, 'shorten.html', context = urloutput)
    else:
        return render(request, 'shorten.html')
