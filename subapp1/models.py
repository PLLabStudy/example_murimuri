from django.db import models

# Create your models here.
class Example(models.Model):
    class Meta:
        verbose_name = '게시물'
        verbose_name_plural = '게시판' 

    title = models.CharField(verbose_name='제목', max_length=250)
    content = models.CharField(verbose_name='내용', max_length=100)
