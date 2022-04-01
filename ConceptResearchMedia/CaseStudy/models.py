from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from ConceptVentures.utils import unique_slug_generator
from ConceptResearchMedia.Service.models import Services

class CaseStudy(models.Model):
    title = models.CharField(max_length=120, verbose_name = 'Title')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    client = models.CharField(max_length=120, verbose_name="Client", blank=True, null=True)
    client_img = models.ImageField(upload_to="Images", verbose_name="Client Image", blank=True, null=True)
    summary = models.TextField(verbose_name='Summary')
    service = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Service')
    img = models.ImageField(upload_to="Images", verbose_name = "Case Study Image")
    body = models.TextField(verbose_name="Body")
    slug = models.SlugField(blank=True, null=True, verbose_name = "Slug")

    def __str__(self):
        return self.title + ' | ' + self.client

    def get_absolute_url(self):
        return reverse("case-study-detail", kwargs={"slug": self.slug})

    def get_related_case_study(self):
        current_case_study_id = self.id #get id of current case study
        service_id =  Services.objects.only('id').get(name=self.service).id #get service id of current case study
        related_case_study = CaseStudy.objects.filter(service=service_id).exclude(id=current_case_study_id).order_by('-created_on', '-modified_on')[:3]
        return related_case_study
    
def slugify_instance_title(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slugify_instance_title, sender=CaseStudy)