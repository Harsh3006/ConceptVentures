from django.shortcuts import render, redirect, reverse,HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from user.models import User
from django.contrib import messages
from .models import Transcriber, TranscriberLanguage, Freelancer, Vendor, VendorCenter, Panelist
from .forms import BasicInformationForm, TranscriberLanguageForm, LocationForm, TranscriberQualificationForm, FreelancerQualificationForm, DocumentsForm, PaymentDetailForm, AgentDetailsForm, AgentCenterForm, PanelistExperienceForm
from django.forms.models import modelformset_factory, inlineformset_factory
import re, urllib

def check_user(user, user_type):
    if (user_type == 'transcriber'):
        if (user.is_transcriber):
            return True, Transcriber
    elif (user_type == 'freelancer'):
        if (user.is_freelancer):
            return True, Freelancer
    elif (user_type == 'vendor'):
        if (user.is_vendor):
            return True, Vendor
    elif (user_type == 'panelist'):
        if (user.is_panelist):
            return True, Panelist
    return False, None

class BasicInformationClass:

    def __init__(self, request, model, user_type):
        self.request = request
        self.model = model
        self.user_type = user_type
        self.redirect_url = self.get_redirect_url()

    def get_redirect_url(self):
        if self.user_type == 'transcriber':
            return 'languages'
        else:
            return 'location'
    
    def BasicInfromationPostView(self):
        BasicInformationForm.Meta.model = self.model
        try:
            current_user = self.model.objects.get(user=self.request.user)
            form = BasicInformationForm(self.request.POST, self.request.FILES, instance=current_user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(self.redirect_url)
            else:
                context = {
                    'form': form,
                    'user_type': self.user_type
                }
                return render(self.request, 'ConceptResearchMedia/account/basic-information.html', context)
        except self.model.DoesNotExist:
            form = BasicInformationForm(self.request.POST, self.request.FILES)
            if form.is_valid():
                instance = self.model()
                for field, value in form.cleaned_data.items():
                    setattr(instance, field, value)
                instance.user = self.request.user
                instance.save()
                return HttpResponseRedirect(self.redirect_url)
            else:
                context = {
                    'form': form,
                    'user_type': self.user_type
                }
                return render(self.request, 'ConceptResearchMedia/account/basic-information.html', context)

    def BasicInformationGetView(self):
        try:
            current_user = self.model.objects.get(user=self.request.user)
        except self.model.DoesNotExist:
            current_user = None
        form = BasicInformationForm(instance=current_user)
        context = {
                    'form': form,
                    'user_type': self.user_type
                }
        return  render(self.request, 'ConceptResearchMedia/account/basic-information.html', context)

@login_required
def BasicInformation(request, user_type):
    user, model = check_user(request.user, user_type)
    if user:
        if (request.method == 'POST'):
            obj = BasicInformationClass(request, model, user_type)
            return obj.BasicInfromationPostView()
        else:
            obj = BasicInformationClass(request, model, user_type)
            return obj.BasicInformationGetView()
    else:
        messages.warning(request, "You are not authorised to view that page!. Please login through correct account")
        return redirect('login')
    
@login_required
@user_passes_test(lambda user: user.is_transcriber)
def TranscriberLanguageView(request):
    try:
        current_user = Transcriber.objects.get(user=request.user)
        TranscriberLanguageFormSet = modelformset_factory(TranscriberLanguage, form=TranscriberLanguageForm, extra=0)
        qs = TranscriberLanguage.objects.filter(transcriber=current_user)
        if request.method == "POST":
            enurl = urllib.parse.urlencode(request.POST)  # To convert POST into a string
            matchobj = re.search(r'del_btn[^\d]*(\d+)', enurl)  # To match for e.g. del_btn1
            if matchobj:
                btn_name = matchobj.group()  # Contains matched button name
                lang_id = ''
                for c in btn_name:
                    if (c.isdigit()):
                        lang_id += c
                query = TranscriberLanguage.objects.get(id=lang_id).delete()
                return redirect('languages')
            formset = TranscriberLanguageFormSet(request.POST, queryset=qs)
            if formset.is_valid():
                instance = TranscriberLanguage()
                for obj in formset.cleaned_data:
                    item_set, id_set = obj.items()
                    field, value = item_set
                    print(field, value)
                    setattr(instance, field, value)
                instance.transcriber = current_user
                instance.save()
                return HttpResponseRedirect('location')
            else:
                return render(request, 'ConceptResearchMedia/account/languages.html', {'formset': formset, 'user_type': 'transcriber'})
        else:
            formset = TranscriberLanguageFormSet(queryset=qs)
            return render(request, 'ConceptResearchMedia/account/languages.html', {'formset': formset, 'user_type': 'transcriber'})
    except Transcriber.DoesNotExist:
        messages.warning(request, 'Please enter your basic details first!')
        return redirect(reverse('basic-information', kwargs={'user_type': 'transcriber'}))
        
class LocationClass:

    def __init__(self, request, model, user_type):
        self.request = request
        self.model = model
        self.user_type = user_type
        self.redirect_url = self.get_redirect_url()

    def get_redirect_url(self):
        if self.user_type == 'vendor':
            return 'documents'
        else:
            return 'qualification'
    
    def LocationPostView(self):
        BasicInformationForm.Meta.model = self.model
        try:
            current_user = self.model.objects.get(user=self.request.user)
            form = LocationForm(self.request.POST, instance=current_user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(self.redirect_url)
            else:
                context = {
                    'form': form,
                    'user_type': self.user_type
                }
                return render(self.request, 'ConceptResearchMedia/account/location.html', context)
        except self.model.DoesNotExist:
            form = LocationForm(self.request.POST)
            if form.is_valid():
                instance = self.model()
                for field, value in form.cleaned_data.items():
                    setattr(instance, field, value)
                instance.user = self.request.user
                instance.save()
                return HttpResponseRedirect(self.redirect_url)
            else:
                context = {
                    'form': form,
                    'user_type': self.user_type
                }
                return render(self.request, 'ConceptResearchMedia/account/location.html', context)

    def LocationGetView(self):
        try:
            current_user = self.model.objects.get(user=self.request.user)
        except self.model.DoesNotExist:
            current_user = None
        form = LocationForm(instance=current_user)
        context = {
                    'form': form,
                    'user_type': self.user_type
                }
        return  render(self.request, 'ConceptResearchMedia/account/location.html', context)

@login_required
def location(request, user_type):
    user, model = check_user(request.user, user_type)
    if user:
        if (request.method == 'POST'):
            obj = LocationClass(request, model, user_type)
            return obj.LocationPostView()
        else:
            obj = LocationClass(request, model, user_type)
            return obj.LocationGetView()
    else:
        messages.warning(request, "You are not authorised to view that page!. Please login through correct account")
        return redirect('login')

def agentDetail(request):
    try:
        current_user = Vendor.objects.get(user=request.user)
        AgentCenterFormSet = modelformset_factory(VendorCenter, form=AgentCenterForm, extra=0)
        qs = VendorCenter.objects.filter(vendor=current_user)
        if request.method == "POST":
            enurl = urllib.parse.urlencode(request.POST)  # To convert POST into a string
            matchobj = re.search(r'del_btn[^\d]*(\d+)', enurl)  # To match for e.g. del_btn1
            if matchobj:
                btn_name = matchobj.group()  # Contains matched button name
                center_id = ''
                for c in btn_name:
                    if (c.isdigit()):
                        center_id += c
                query = VendorCenter.objects.get(id=center_id).delete()
                return redirect('agent-detail')
            form = AgentDetailsForm(request.POST, instance=current_user)
            formset = AgentCenterFormSet(request.POST, queryset=qs)
            if form.is_valid() and formset.is_valid():
                form.save()
                instance = VendorCenter()
                for obj in formset.cleaned_data:
                    item_set, id_set = obj.items()
                    field, value = item_set
                    setattr(instance, field, value)
                instance.vendor = current_user
                instance.save()
                return HttpResponseRedirect('documents')
            else:
                return render(request, 'ConceptResearchMedia/account/agent-detail.html', {'form': form, 'formset': formset, 'user_type': 'vendor'})
        else:
            form = AgentDetailsForm(instance=current_user)
            formset = AgentCenterFormSet(queryset=qs)
            return render(request, 'ConceptResearchMedia/account/agent-detail.html', {'form': form, 'formset': formset, 'user_type': 'vendor'})
    except Vendor.DoesNotExist:
        messages.warning(request, 'Please enter your basic details first!')
        return redirect(reverse('basic-information', kwargs={'user_type': 'vendor'}))

class QualificationClass:

    def __init__(self, request, model, user_type):
        self.request = request
        self.model = model
        self.user_type = user_type
        self.form = self.get_form()

    def get_form(self):
        if self.user_type == 'transcriber':
            return TranscriberQualificationForm
        elif self.user_type == 'freelancer':
            return FreelancerQualificationForm
        elif self.user_type == 'panelist':
            return PanelistExperienceForm

    def QualificationPostView(self):
        try:
            current_user = self.model.objects.get(user=self.request.user)
            form = self.form(self.request.POST, instance=current_user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('documents')
            else:
                context = {
                    'form': form,
                    'user_type': self.user_type
                }
                return render(self.request, 'ConceptResearchMedia/account/qualification.html', context)
        except self.model.DoesNotExist:
            form = self.form(self.request.POST)
            if form.is_valid():
                instance = self.model()
                for field, value in form.cleaned_data.items():
                    setattr(instance, field, value)
                instance.user = self.request.user
                instance.save()
                return HttpResponseRedirect('documents')
            else:
                context = {
                    'form': form,
                    'user_type': self.user_type
                }
                return render(self.request, 'ConceptResearchMedia/account/qualification.html', context)

    def QualificationGetView(self):
        try:
            current_user = self.model.objects.get(user=self.request.user)
        except self.model.DoesNotExist:
            current_user = None
        form = self.form(instance=current_user)
        context = {
                    'form': form,
                    'user_type': self.user_type
                }
        return  render(self.request, 'ConceptResearchMedia/account/qualification.html', context)

@login_required
def Qualification(request, user_type):
    user, model = check_user(request.user, user_type)
    if user:
        if (request.method == 'POST'):
            obj = QualificationClass(request, model, user_type)
            return obj.QualificationPostView()
        else:
            obj = QualificationClass(request, model, user_type)
            return obj.QualificationGetView()
    else:
        messages.warning(request, "You are not authorised to view that page!. Please login through correct account")
        return redirect('login')

class DocumentsClass:

    def __init__(self, request, model, user_type):
        self.request = request
        self.model = model
        self.user_type = user_type
    
    def DocumentsPostView(self):
        DocumentsForm.Meta.model = self.model
        try:
            current_user = self.model.objects.get(user=self.request.user)
            form = DocumentsForm(self.request.POST, self.request.FILES, instance=current_user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('payment-details')
            else:
                context = {
                    'form': form,
                    'user_type': self.user_type
                }
                return render(self.request, 'ConceptResearchMedia/account/documents.html', context)
        except self.model.DoesNotExist:
            form = DocumentsForm(self.request.POST)
            if form.is_valid():
                instance = self.model()
                for field, value in form.cleaned_data.items():
                    setattr(instance, field, value)
                instance.user = self.request.user
                instance.save()
                return HttpResponseRedirect('payment-details')
            else:
                context = {
                    'form': form,
                    'user_type': self.user_type
                }
                return render(self.request, 'ConceptResearchMedia/account/documents.html', context)

    def DocumentsGetView(self):
        try:
            current_user = self.model.objects.get(user=self.request.user)
        except self.model.DoesNotExist:
            current_user = None
        form = DocumentsForm(instance=current_user)
        context = {
                    'form': form,
                    'user_type': self.user_type
                }
        return  render(self.request, 'ConceptResearchMedia/account/documents.html', context)

@login_required
def documents(request, user_type):
    user, model = check_user(request.user, user_type)
    if user:
        if (request.method == 'POST'):
            obj = DocumentsClass(request, model, user_type)
            return obj.DocumentsPostView()
        else:
            obj = DocumentsClass(request, model, user_type)
            return obj.DocumentsGetView()
    else:
        messages.warning(request, "You are not authorised to view that page!. Please login through correct account")
        return redirect('login')

class PaymentDetailClass:
    def __init__(self, request, model, user_type):
        self.request = request
        self.model = model
        self.user_type = user_type
    
    def PaymentDetailPostView(self):
        PaymentDetailForm.Meta.model = self.model
        try:
            current_user = self.model.objects.get(user=self.request.user)
            form = PaymentDetailForm(self.request.POST, self.request.FILES, instance=current_user)
            if form.is_valid():
                form.save()
                return redirect(reverse('basic-information', kwargs={'user_type': self.user_type}))
            else:
                context = {
                    'form': form,
                    'user_type': self.user_type
                }
                return render(self.request, 'ConceptResearchMedia/account/payment-details.html', context)
        except self.model.DoesNotExist:
            form = PaymentDetailForm(self.request.POST)
            if form.is_valid():
                instance = self.model()
                for field, value in form.cleaned_data.items():
                    setattr(instance, field, value)
                instance.user = self.request.user
                instance.save()
                return redirect(reverse('basic-information', kwargs={'user_type': self.user_type}))
            else:
                context = {
                    'form': form,
                    'user_type': self.user_type
                }
                return render(self.request, 'ConceptResearchMedia/account/payment-details.html', context)

    def PaymentDetailGetView(self):
        try:
            current_user = self.model.objects.get(user=self.request.user)
        except self.model.DoesNotExist:
            current_user = None
        form = PaymentDetailForm(instance=current_user)
        context = {
                    'form': form,
                    'user_type': self.user_type
                }
        return  render(self.request, 'ConceptResearchMedia/account/payment-details.html', context)

@login_required
def PaymentDetail(request, user_type):
    user, model = check_user(request.user, user_type)
    if user:
        if (request.method == 'POST'):
            obj = PaymentDetailClass(request, model, user_type)
            return obj.PaymentDetailPostView()
        else:
            obj = PaymentDetailClass(request, model, user_type)
            return obj.PaymentDetailGetView()
    else:
        messages.warning(request, "You are not authorised to view that page!. Please login through correct account")
        return redirect('login')