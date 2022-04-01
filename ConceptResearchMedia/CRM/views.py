from django.shortcuts import render
from meta.views import Meta
from ConceptResearchMedia.Blog.models import BlogPost
from ConceptResearchMedia.CaseStudy.models import CaseStudy
from ConceptResearchMedia.TeamMembers.models import TeamMembers
from django.views.decorators.csrf import csrf_protect
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings

def CRMIndex(request):
    member_set = TeamMembers.objects.all().filter(is_display=True)
    recent_blog_post = BlogPost.objects.all().order_by('-created_on', '-modified_on')[:6]
    recent_case_study = CaseStudy.objects.all().order_by('-created_on', '-modified_on')[:6]
    context = {
            "meta": Meta(
                use_og=True,
                use_facebook=True,
                og_title='Welcome to Concept Research Media',
                description='Concept Research Media specializes in providing state-of-art B2B & B2C market research, consulting and problem solving services.',
                url='', 
                image='',
                object_type='website',
            ),
            'member_set': member_set,
            'recent_blog_post': recent_blog_post, 
            'recent_case_study': recent_case_study

         }
    return render(request, 'ConceptResearchMedia/index.html', context)

def CRMAbout(request):
    member_set = TeamMembers.objects.all().filter(is_display=True)
    context = {
            "meta": Meta(
                use_og=True,
                use_facebook=True,
                og_title='About Concept Research Media',
                description='Concept Research Media specializes in providing state-of-art B2B & B2C market research, consulting and problem solving services.',
                url='', 
                image='',
                object_type='website',
            ),
            'member_set': member_set
         }
    return render(request, 'ConceptResearchMedia/about.html', context)

@csrf_protect
def contact(request):
    if (request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']
        phone_no = request.POST['phone-no']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(subject, message, email, [settings.EMAIL_FROM_USER])
        return render(request, 'contact.html', {'name': name})
    else:
        context = {
            "meta": Meta(
                use_og=True,
                use_facebook=True,
                og_title='Contact Concept Research Media',
                description='Have a query or want to know more? Contact Us!',
                url='', 
                image='',
                object_type='website',
            )
         }
        return render(request, 'ConceptResearchMedia/contact.html', context)

def work_with_us(request):
    recent_blog_post = BlogPost.objects.all().order_by('-created_on', '-modified_on')[:6]
    recent_case_study = CaseStudy.objects.all().order_by('-created_on', '-modified_on')[:6]
    return render(request, 'ConceptResearchMedia/work-with-us.html', context={'recent_blog_post': recent_blog_post, 'recent_case_study': recent_case_study})
    
def PrivacyPloicy(request):
    return render(request, 'ConceptResearchMedia/privacy-policy.html')