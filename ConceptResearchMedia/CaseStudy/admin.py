from django.contrib import admin
from .models import CaseStudy

class CaseStudyAdmin(admin.ModelAdmin):
    class Media:
        js = ('JS/tinyMce.js',)

admin.site.register(CaseStudy, CaseStudyAdmin)