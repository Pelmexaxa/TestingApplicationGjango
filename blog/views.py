from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import requests

from .models import *

url_user = 'http://jsonplaceholder.typicode.com/users'
url_post = 'http://jsonplaceholder.typicode.com/posts'

user_data = requests.get(url_user).json()
post_data = requests.get(url_post).json()

def main(request):
    
    for person in user_data:
        temp = BlogPerson(id = person.get('id'), name = person.get('name'))
        temp.save()
    
    for post in post_data:
        temp = BlogNews(id = post.get('id'), 
                 title = post.get('title'),
                 content = post.get('body'),
                 userId = post.get('userId'))
        temp.save()
        
    person = BlogPerson.objects.all()
    post = BlogNews.objects.all()
    
    # return HttpResponse("404")
    return render(request, 'blog/main.html', {'person': person, 'post': post, 'styleTr': True})
