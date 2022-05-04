from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
#from .models import UrlToShort
from .functions import CheckDbOrAdd


# Create your views here.

def Home(request):
    return render(request, 'base.html')

@csrf_exempt
def Shorten(request):
    if request.method == 'POST':
        inputurl = request.POST.get('inputurl')
        outputurl = CheckDbOrAdd(inputurl)
        urloutput = {'output': outputurl}
        return render(request, 'shorten.html', context = urloutput)
    else:
        return render(request, 'shorten.html')
