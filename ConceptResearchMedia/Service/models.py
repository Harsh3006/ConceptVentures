from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=200)
    dept_choice = (
        ('Market Research', 'Market Research'),
        ('Content Writing & Transcription','Content Writing & Transcription'),
        ('Data Analytics','Data Analytics'),
        ('Panel Service','Panel Service'),
        ('Industry Report','Industry Report'),
        ('Survey Creation','Survey Creation')
    )
    department = models.CharField(max_length=200, choices=dept_choice, null=True, blank=True, verbose_name='Department')
    def __str__(self):
        return self.name
