from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import requests

from .models import *

def main(request):
        
    person = BlogPerson.objects.all()
    post = BlogNews.objects.all()

    # return HttpResponse("404")
    return render(request, 'blog/main.html', {'post': post})
