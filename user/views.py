from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from meta.views import Meta
from user.models import User
from django.contrib.auth.models import auth
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from .utils import generate_token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings

# All Users Views
def activate_user(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()
        messages.success(request, 'Email verified! You can login now')
        return redirect('login')
    else:
        messages.error(request, 'Email verification failed')
        return redirect('send-verification-email')

@csrf_protect
def login(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            if (user.is_email_verified):
                if (user.is_transcriber):
                    auth.login(request, user)
                    return redirect(reverse('basic-information', kwargs={'user_type': 'transcriber'}))
                elif (user.is_freelancer):
                    auth.login(request, user)
                    return redirect(reverse('basic-information', kwargs={'user_type': 'freelancer'}))
                elif (user.is_vendor):
                    auth.login(request, user)
                    return redirect(reverse('basic-information', kwargs={'user_type': 'vendor'}))
                elif (user.is_panelist):
                    auth.login(request, user)
                    return redirect(reverse('basic-information', kwargs={'user_type': 'panelist'}))
                else:
                    return HttpResponse('You are not authorised to view this page')
            else:
                messages.warning(request, 'Please verify your email first')
                return redirect('send-verification-email')
        else:
            messages.error(request, 'Invalid Email or Password')
            return redirect('login')
    else:
        context = {
            "meta": Meta(
                use_og=True,
                use_facebook=True,
                og_title='Login',
                description='Login to your CRM account!',
                url='', 
                image='',
                object_type='website',
            )
         }
        return render(request, 'User/login.html', context)

@csrf_protect
def signup(request, user_type):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        country = request.POST['country']

        if User.objects.filter(email= email).exists():
            messages.info(request, 'Email already exists')
            return redirect(reverse('signup', kwargs={'user_type':user_type}))
        else:
            user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, country=country)
            if (user_type=='transcriber'):
                user.is_transcriber = True
            elif (user_type=='freelancer'):
                user.is_freelancer = True
            elif (user_type=='vendor'):
                user.is_vendor = True
            elif (user_type=='panelist'):
                user.is_panelist = True
            else:
                return HttpResponse('Invalid user type!')
            user.save()
            SendVerificationEmail(request, user, email)
            return render(request, 'User/email-verify-message.html', {'email': email, 'status': 'pre'})
    else:
        context = {
            "meta": Meta(
                use_og=True,
                use_facebook=True,
                og_title='Signup',
                description='Create your CRM account',
                url='', 
                image='',
                object_type='website',
            ),
            'user_type': user_type
         }
        return render(request, 'User/signup.html', context)

def ResendVerificationEmail(request):
    if (request.method == "POST"):
        email = request.POST['email']
        if not User.objects.filter(email= email).exists():
            messages.error(request, 'Invalid Email')
            return redirect('send-verification-email')
        else:
            user = User.objects.filter(email=email)[0]
            SendVerificationEmail(request, user, email)
            return render(request, 'User/email-verify-message.html', {'email': email, 'status': 'post'})
    else:
        return render(request, 'User/verification-email.html')
            
def SendVerificationEmail(request, user, email):
    current_site = get_current_site(request)
    email_subject = "You're Almost There! Confirm Email"
    email_body = render_to_string('User/activate.html', {
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user)
            })

    # send_mail(subject, message, from_email, recipient_list)
    send_mail(email_subject, email_body, settings.EMAIL_FROM_USER, [email])

def logout(request):
    auth.logout(request)
    return redirect('crm-index')

def RequestPasswordReset(request):
    if request.method=="POST":
        email = request.POST['email']
        if not User.objects.filter(email= email).exists():
            messages.error(request, 'Invalid Email')
            return redirect('reset-password')
        else:
            user = User.objects.filter(email=email)[0]
            if not user.is_email_verified:
                messages.warning(request, 'Please verify your email first to activate your account')
                return redirect('reset-password')
            else:
                current_site = get_current_site(request)
                email_subject = "Concept research Media -  Reset Password Instructions"
                email_body = render_to_string('User/request-reset-password.html', {
                    'domain': current_site,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': PasswordResetTokenGenerator().make_token(user)
                })
                send_mail(email_subject, email_body, settings.EMAIL_FROM_USER, [user.email])
                messages.success(request, 'We have sent you an email to reset your password. Please also check in spam.')
                return redirect('login')
    else:
        return render(request, 'User/reset-password.html')

def RenderResetPasswordTemplate(request, uidb64, token):
    context={
            'uidb64': uidb64,
            'token': token
        }
    if request.method=="POST":
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.error(request, 'Password not matching')
            return render(request, 'User/newpassword.html', context)
        else:
            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
                user.set_password(password1)
                user.save()
                messages.success(request, 'Password Changed, you can login now')
                return redirect('login')
            except Exception as e:
                messages.error(request, 'Something went wrong')
                return redirect('reset-password')
    else:
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            if not PasswordResetTokenGenerator().check_token(user, token):
                messages.warning(request, 'Link Expired. You can request a new one.')
                return redirect('reset-password')
        except:
            messages.error(request, 'Something went wrong')
            return redirect('reset-password')
    return render(request, 'User/newpassword.html', context)