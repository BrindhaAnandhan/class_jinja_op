from django.shortcuts import render

# Create your views here.

def generic(request):
    return render(request, 'generic.html')
def sep(request):
    return render(request, 'sep.html')

