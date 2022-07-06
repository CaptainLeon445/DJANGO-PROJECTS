from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='profile',blank=False)
    profession=models.CharField(max_length=50)
    about=models.CharField(max_length=300)

    def __str__(self):
        return self.user.username

class projects(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    picture=models.ImageField(upload_to='portfolio',blank=False)
    description=models.CharField(max_length=500)
    

    def __str__(self):
        return self.title

class contact(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    subject=models.CharField(max_length=80)
    email=models.EmailField()
    to=models.EmailField()
    message=models.TextField()
    sent=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('sent',)


