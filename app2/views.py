from django.shortcuts import render

# Create your views here.
def response (request):
    return render (request, "response_page.html")