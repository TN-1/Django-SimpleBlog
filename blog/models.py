from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    description = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    ordering=['-created']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return 'blog/%s' % self.slug
        #return reverse('blog:post', kwargs={'slug':self.slug})
        #commented return throws u'blog' is not a registered namespace

class BlogInfo(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    def __str__(self):
        return self.name
    def getname(self):
        return '%s' % self.name
    def getabout(self):
        return '%s' % self.about
