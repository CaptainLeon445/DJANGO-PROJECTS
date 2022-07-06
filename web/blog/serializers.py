from rest_framework import serializers
from .models import Comment,Post,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name','slug']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['id','title','slug','author','body','category','tags','created','updated']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['id','name','body','post','created']