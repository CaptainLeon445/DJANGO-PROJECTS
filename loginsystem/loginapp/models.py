from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class SavePassword(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,)
    password=models.CharField(max_length=200) 
    created=models.DateField(default=timezone.now)

    class Meta:
        ordering=('-created',)

    def __str__(self):
        return self.title

    def get_absolute_uri(self):
        return reverse('loginapp:pwd_detail',
        args=[self.created.year, self.created.day, self.created.month, self.slug,self.id])
