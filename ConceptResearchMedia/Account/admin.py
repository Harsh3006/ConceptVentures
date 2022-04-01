from django.contrib import admin
from .models import Employee, Transcriber,TranscriberLanguage, Freelancer, Vendor, Panelist

admin.site.register(Employee)
admin.site.register(Transcriber)
admin.site.register(TranscriberLanguage)
admin.site.register(Freelancer)
admin.site.register(Vendor)
admin.site.register(Panelist)