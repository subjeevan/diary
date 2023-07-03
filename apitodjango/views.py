from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class ContactAPIView(APIView):
    def get(self,request):
        response=request.get('http://localhost:8000/contactapi/data')
        if response.status_code==200:
            data =response.json()


def apitodjango(request):
    url='http://localhost:8000/contactapi/data'

    response=request.get(url)
    data=response.json()
    return render(request,'apidata.html',{'data':data})