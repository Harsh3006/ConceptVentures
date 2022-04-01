from django.db import models
from user.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.timezone import now

class Employee(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Employee')
    manager = models.OneToOneField(User, blank=True, null=True, default=None, on_delete=models.SET_DEFAULT, related_name='Manager', verbose_name='Employee Manager')

    def __str__(self):
        return self.employee.first_name + ' ' + self.employee.last_name
    
# Common Field for all users
class BasicDetails(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(default=now, verbose_name='Date of Birth')
    phone_number = PhoneNumberField(default='')
    linkedin_profile = models.URLField(blank=True, null=True, verbose_name='Linkedin Profile')
    profile_picture = models.ImageField(upload_to="Images", null=True, blank=True, verbose_name="Profile Picture")
    # address
    city = models.CharField(max_length=100, default='', verbose_name='City')
    state = models.CharField(max_length=100, default='', verbose_name='State')
    postal_code = models.CharField(max_length=10, default='', verbose_name='Postal Code')
    street = models.TextField(default='', verbose_name='Street Address')
    # identification documents
    aadhar_card = models.FileField(upload_to='Documents', null=True, blank=True, verbose_name="Aadhar Card")
    pan_card = models.FileField(upload_to='Documents', null=True, blank=True, verbose_name = 'Pan Card')
    passport = models.FileField(upload_to='Documents', null=True, blank=True, verbose_name = 'Passport')
    # payment_details
    account_holder = models.CharField(max_length=200, default='', verbose_name='Account Holder')
    ac_no = models.CharField(max_length=18, default='', verbose_name='Account Number')
    ifsc_code = models.CharField(max_length=11, default='', verbose_name='IFSC Code')
    swift_code = models.CharField(max_length=11, default='', verbose_name='SWIFT Code')

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    
experience_choice = (
        ('0', '0 Year'),
        ('1', '1 Year'),
        ('2', '2 Years'),
        ('3', '3 Years'),
        ('4', '4 Years'),
        ('5+', '5+ Years')
    )
qualification_choice = (
    ('underGrad Pursuing', 'Undergraduate Pursuing'),
    ('underGrad Completed', 'Undergraduate Completed'),
    ('postGrad Pursuing', 'Postgraduation Pursuing'),
    ('postGrad Completed', 'Postgraduation Completed'),
    ('diploma', 'Diploma')
)
class Transcriber(BasicDetails):
    skilled_choices = (
        ('Content Writing', 'Content Writing'),
        ('Transcription','Transcription'),
        ('Translation','Translation'),
        ('Audio Recording','Audio Recording'),
        ('Video Recording','Video Recording'),
        ('Annotation','Annotation'),
        ('Subtitling','Subtitling')
    )
    skills = models.CharField(max_length=50, choices=skilled_choices, default='', verbose_name='Skilled In')
    experience = models.CharField(max_length=10, choices=experience_choice, default='', verbose_name='Experience')
    qualification = models.CharField(max_length=50, choices=qualification_choice, default='', verbose_name='Qualification')

class TranscriberLanguage(models.Model):
    transcriber = models.ForeignKey(Transcriber, on_delete=models.CASCADE)    
    language = models.CharField(max_length=50, default='', verbose_name='Language')

    def __str__(self):
        return self.language
    
class Freelancer(BasicDetails):
    skilled_choices = (
        ('Market Research', 'Market Research'),
        ('Data Research', 'Data Research')
    )
    qualification = models.CharField(max_length=50, choices=qualification_choice, default='', verbose_name='Qualification')
    experience = models.CharField(max_length=10, choices=experience_choice, default='', verbose_name='Experience')
    company_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Company Worked With')
    skills = models.CharField(max_length=50, choices=skilled_choices, default='', verbose_name='Skilled In')
    moderator = models.BooleanField(default=False, verbose_name='Is Moderator')
    type_of_project = models.CharField(max_length=300, default='', verbose_name='Type of Project')
    associated_company = models.CharField(max_length=200, null=True, blank=True, verbose_name='Company Associated With')

class Vendor(BasicDetails):
    agency_name = models.CharField(max_length=100, default='', verbose_name='Agency Name')
    team_size = models.CharField(max_length=20, default='', verbose_name='Team Size')
    type_of_project = models.CharField(max_length=100, default='', verbose_name='Type of Project')
    hq = models.CharField(max_length=100, default='', verbose_name='Headquarter')
    website = models.URLField(default='', verbose_name='Website')

class VendorCenter(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    center = models.CharField(max_length=100, default='', verbose_name='Center')

class Panelist(BasicDetails):
    experience = models.CharField(max_length=100, default='', verbose_name='Experienced in Vertical')
    company_association = models.BooleanField(default=False, verbose_name='Associated with any company')
    retired = models.BooleanField(default=False, verbose_name='Is Retired')
    one_to_one_conv = models.BooleanField(default=False, verbose_name='Comfortable in One to One Conversation')
    group_discussion = models.BooleanField(default=False, verbose_name='Comfortable in Group Discussion')
    email_survey = models.BooleanField(default=False, verbose_name='Comfortable in Email Surveys')
    telephonic_interview = models.BooleanField(default=False, verbose_name='Comfortable in Telephonic Interview')