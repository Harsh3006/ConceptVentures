from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from ConceptVentures.utils import unique_slug_generator

class TeamMembers(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Full Name')
    designation = models.CharField(max_length=200)
    profile_img = models.ImageField(upload_to = 'Images', verbose_name = 'Profile Picture')
    bio = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True, verbose_name="Facebook Profile URL")
    twitter = models.URLField(blank=True, null=True, verbose_name="Twitter Profile URL")
    linkedin = models.URLField(blank=True, null=True, verbose_name="Linkedin Profile URL")
    is_display = models.BooleanField(default=True)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("member-detail", kwargs={"slug": self.slug})

def slugify_instance_name(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slugify_instance_name, sender=TeamMembers)
    