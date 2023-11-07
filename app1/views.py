from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def jampandu(request):
    return HttpResponse('<h1><marquee>hii jampandu</marquee></h1>')
 
def heroine(request):
    return HttpResponse('<h1> HII KRITHI SHETTY </h1>')
