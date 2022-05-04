from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def Home(request):
    return render(request, 'base.html')

@csrf_exempt
def Shorten(request):
    if request.method == 'POST':
        response = request.POST.get('inputurl')
        print(response)
        urloutput = {'output': ""}
        return render(request, 'shorten.html', context = urloutput)
    else:
        return render(request, 'shorten.html')
