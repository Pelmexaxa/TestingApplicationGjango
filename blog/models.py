from django.db import models

class BlogPerson(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class BlogNews(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField(blank=True)
    userId = models.IntegerField()
    
    def __str__(self):
        return self.userId