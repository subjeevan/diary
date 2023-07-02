from django.shortcuts import render
from django.http import HttpResponse
from contact.models import Contact

# Create your views here.

def showcontactapi(request):
    contact=Contact.objects.get()
    return HttpResponse("wElocme ")