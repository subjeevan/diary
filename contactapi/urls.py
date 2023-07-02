from django.urls import path
from .views import showcontactapi

urlpatterns = [
   
   path('showcontactapi/',showcontactapi,name='showcontactapi'),
   ]
