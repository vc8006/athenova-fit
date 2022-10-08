from django.contrib import admin
from .models import Image,User

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','photo','date']

@admin.register(User)
class USerAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone']
