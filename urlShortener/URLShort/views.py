from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models



# Create your views here.

def Home(request):
    return render(request, 'base.html')

@csrf_exempt
def Shorten(request):
    if request.method == 'POST':
        response = request.POST.get('inputurl')
        url = models.UrlToShort()
        url.inputurl = response
        url.outputurl = url.shortenurl(response)
        print(response)
        urloutput = {'output': url.outputurl}
        return render(request, 'shorten.html', context = urloutput)
    else:
        return render(request, 'shorten.html')
