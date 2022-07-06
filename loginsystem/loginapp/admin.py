


from django.contrib import admin
from .models import SavePassword

@admin.register(SavePassword)
class SavePasswordAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug','password',]
    prepopulated_fields = {'slug': ('title',)}