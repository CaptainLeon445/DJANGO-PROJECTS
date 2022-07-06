from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=25)
    slug=models.SlugField(max_length=25)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:post_list_by_category', args=[self.slug])



class Post(models.Model):
    title=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField(max_length=1000)
    #image=models.ImageField(upload_to='path',blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    class Meta:
        ordering=('-created',)
    def __str__(self):
        return self.title
        
 

    def get_absolute_url(self):
        return reverse('blog:postdetail',args=[self.id,self.slug])

class Comment(models.Model):
    name=models.CharField(max_length=30)
    body=models.TextField(max_length=300)
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-created',)
    def __str__(self):
        return self.name
