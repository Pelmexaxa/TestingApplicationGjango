from django.db import models

class BlogNews(models.Model):
    title = models.CharField(max_length = 200, verbose_name = 'Заголовок')
    content = models.TextField(blank=True, verbose_name = 'Контент')
    userId = models.ForeignKey('BlogPerson', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['id']
        
class BlogPerson(models.Model):
    name = models.CharField(max_length = 100, db_index=True)

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'