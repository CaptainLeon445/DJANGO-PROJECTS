from django.contrib import admin
from .models import Category, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',]
    prepopulated_fields = {'slug': ('name',)}
    
class ModuleInline(admin.StackedInline):
    model = Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'created','tags']
    list_filter = ['created', 'author']
    search_fields = ['title', 'body','author']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'body', 'created']
    list_filter = ['post',]