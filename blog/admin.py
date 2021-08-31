from django.contrib import admin

from .models import *

class BlogNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'userId')
    list_display_links = ('id', 'title')
    

admin.site.register(BlogPerson)
admin.site.register(BlogNews, BlogNewsAdmin)