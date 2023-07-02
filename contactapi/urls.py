from django.urls import path
from .views import showcontactapi,Dataedit,Datalist

urlpatterns = [
   
   path('showcontactapi/',showcontactapi,name='showcontactapi'),
   path('data',Datalist.as_view,name='data'),
   ]
