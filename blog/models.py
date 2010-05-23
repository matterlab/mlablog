#coding=utf-8
from django.db import models

class Post(models.Model):    
    title = models.CharField(u'标题',max_length=255)
    content = models.TextField(u'内容')
    pubdate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-pubdate']
        verbose_name=u'文章'
        verbose_name_plural = u'文章'
