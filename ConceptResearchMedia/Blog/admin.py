from django.contrib import admin
from .models import BlogCategory, BlogPost
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ("JS/tinyMce.js",)

admin.site.register(BlogCategory)
admin.site.register(BlogPost, BlogAdmin)

