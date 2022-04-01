from django import forms
from .models import BasicDetails, Transcriber, TranscriberLanguage, Freelancer, Vendor, VendorCenter, Panelist
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class BasicInformationForm(forms.ModelForm):
    required_css_class = 'required'
    dob = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))
    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='IN', attrs={'class': 'phone-number'}))
    linkedin_profile = forms.URLField(required=False)
    profile_picture = forms.FileField(required=False, widget=forms.FileInput(attrs={'accept':'image/jpg, image/jpeg, image/.png'}), help_text='Accept .jpg, .jpeg, .png formats only')
    class Meta:
        model = BasicDetails #this willl change based on the user type from views
        fields = ['dob', 'phone_number', 'linkedin_profile', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({'class': 'input-field'})
        self.fields['phone_number'].widget.attrs.update({'class': 'phone-number'})

class TranscriberLanguageForm(forms.ModelForm):
    required_css_class = 'required'
    language = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field'}))

    class Meta:
        model = TranscriberLanguage
        fields = ['language']
        
class LocationForm(forms.ModelForm):
    required_css_class = 'required' 
    class Meta:
        model = BasicDetails
        fields = ['street', 'city', 'state', 'postal_code']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({'class': 'input-field'})

class TranscriberQualificationForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Transcriber
        fields = ['qualification', 'skills', 'experience']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({'class': 'input-field'})

class FreelancerQualificationForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Freelancer
        fields = ['qualification', 'skills', 'experience', 'company_name', 'moderator', 'type_of_project', 'associated_company']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({'class': 'input-field'})

class PanelistExperienceForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Panelist
        fields = ['experience', 'company_association', 'retired', 'one_to_one_conv', 'group_discussion', 'email_survey', 'telephonic_interview']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({'class': 'input-field'})

class AgentDetailsForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Vendor
        fields = ['agency_name', 'team_size', 'type_of_project', 'hq', 'website']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({'class': 'input-field'})

class AgentCenterForm(forms.ModelForm):
    required_css_class = 'required'
    center = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field'}))

    class Meta:
        model = VendorCenter
        fields = ['center']

class DocumentsForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = BasicDetails
        fields = ['aadhar_card', 'pan_card', 'passport']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({'class': 'input-field'})

class PaymentDetailForm(forms.ModelForm):
    required_css_class = 'required'
    ifsc_code = forms.CharField(required=False)
    class Meta:
        model = BasicDetails
        fields = ['account_holder', 'ac_no', 'ifsc_code', 'swift_code']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({'class': 'input-field'})