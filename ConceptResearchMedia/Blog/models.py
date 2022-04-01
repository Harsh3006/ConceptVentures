from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from ConceptVentures.utils import unique_slug_generator

class BlogCategory(models.Model):
    name = models.CharField(max_length=120, verbose_name = 'Category Name')

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=120, verbose_name = 'Title')
    body = models.TextField(verbose_name="Body")
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name='Category')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    snippet = models.TextField(verbose_name='Summary')
    img = models.ImageField(upload_to='Images', verbose_name="Blog Image")
    slug = models.SlugField(max_length=200, blank=True, null=True, verbose_name = 'Slug')

    class meta:
        ordering = ['-created_on', '-modified_on']

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"slug": self.slug})  

    def get_related_blog_post(self):
        current_blog_post_id = self.id #get id of current blog post
        category_id =  BlogCategory.objects.only('id').get(name=self.category).id #get category id of current blog post
        related_blog_post = BlogPost.objects.filter(category=category_id).exclude(id=current_blog_post_id).order_by('-created_on', '-modified_on')[:3]
        return related_blog_post

def slugify_instance_title(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slugify_instance_title, sender=BlogPost)
