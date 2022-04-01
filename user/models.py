from django.db import models
from django.urls import reverse
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from datetime import datetime
from django.utils import timezone
now = timezone.now()

# All User model (used for authentication)
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, country, password=None, is_staff=False, is_admin=False, is_active=True, is_email_verified=False):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a pasword')
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            country = country
        )
        user.set_password(password)  #encoding the password
        user.first_name = first_name
        user.last_name = last_name 
        user.country = country
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.is_email_verified = is_email_verified
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, last_name, country, password=None):
        user = self.create_user(
            email, 
            first_name = first_name,
            last_name = last_name,
            country = country,
            password=password,
            is_staff = True,
            is_email_verified = True
            )
        return user

    def create_superuser(self, email, first_name, last_name, country, password=None):
        user = self.create_user(
            email, 
            first_name = first_name,
            last_name = last_name,
            country = country,
            password=password,
            is_staff = True,
            is_admin = True,
            is_email_verified = True
            )
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email Address', max_length=255, unique=True)
    first_name = models.CharField(verbose_name='First Name', max_length=100)
    last_name = models.CharField(verbose_name='Last Name', max_length=100)
    country = models.CharField(max_length=100, default='India', verbose_name = 'Country')
    is_email_verified = models.BooleanField(default=False)
    active = models.BooleanField(default=True)   #can login
    staff = models.BooleanField(default=False)   #staff user non-superuser
    admin = models.BooleanField(default=False)   #superuser
    date_joined = models.DateTimeField(verbose_name='Date Joined', blank=True, null=True, default=datetime.now)
    is_employee = models.BooleanField(default=False, verbose_name='Is Employee')
    is_transcriber = models.BooleanField(default=False, verbose_name='Is Transcriber')
    is_vendor = models.BooleanField(default=False, verbose_name='Is Vendor')
    is_freelancer = models.BooleanField(default=False, verbose_name='Is Freelancer')
    is_panelist = models.BooleanField(default=False, verbose_name='Is Panelist')
    objects = UserManager()

    USERNAME_FIELD = 'email'
    #email and password are required by default
    REQUIRED_FIELDS = ['first_name', 'last_name'] 

    def __str__(self):
        return self.first_name + ' ' + self.last_name 

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name + ' | ' + self.email
    
    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active