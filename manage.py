#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import requests
import blog


url_user = 'http://jsonplaceholder.typicode.com/users'
url_post = 'http://jsonplaceholder.typicode.com/posts'

user_data = requests.get(url_user).json()
post_data = requests.get(url_post).json()

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysitetest.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    
    # Загрузка данных
    get_data()

def get_data():
   
    for person in user_data:
        temp_person = blog.models.BlogPerson(id = person.get('id'), name = person.get('name'))
        temp_person.save()
        for post in post_data:
            if person.get('id') == post.get('userId'):
                temp_post = blog.models.BlogNews(id = post.get('id'), 
                         title = post.get('title'),
                         content = post.get('body'),
                         userId_id = person.get('id'))
            temp_post.save()
    
if __name__ == '__main__':
    main()
