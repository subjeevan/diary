"""
URL configuration for diary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import show_data,delete_data,savedata

urlpatterns = [
    path('show_data',show_data,name='show_data'),
    path('show_data/<int:id>/',show_data,name='edit_data'),
    path('delete_data/<int:id>/',delete_data,name='delete_data'),
    path('savedata/',savedata,name='savedata')
]
