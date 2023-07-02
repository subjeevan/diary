from django.shortcuts import render
from django.http import HttpResponse
from contact.models import Contact
from .serializers import Dataserializer
from rest_framework import generics
# Create your views here.

def showcontactapi(request):
    contact=Contact.objects.get(id=1)
    
    return render(request, 'test.html',{'contact':contact})

class Datalist(generics.ListCreateAPIView):
    queryset= Contact.objects.all()
    serializer_class=Dataserializer

class Dataedit(generics.RetrieveUpdateDestroyAPIView):
    queryset= Contact.objects.all()
    serializer_class= Dataserializer