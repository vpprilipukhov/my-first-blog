from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf.urls import  url


urlpatterns = [

    url(r'^', include('bboard.urls')),
    path('admin/', admin.site.urls),
    path('bboard/',include('bboard.urls')),

]


