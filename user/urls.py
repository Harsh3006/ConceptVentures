from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login, name='login'),
    path('signup/<str:user_type>', views.signup, name='signup'), 
    path('send-verification-email', views.ResendVerificationEmail, name='send-verification-email'),
    path('activate-user/<uidb64>/<token>', views.activate_user, name='activate'),
    path('resest-password', views.RequestPasswordReset, name='reset-password'),
    path('request-reset-password/<uidb64>/<token>', views.RenderResetPasswordTemplate, name='request-reset-password'),
    path('logout', views.logout, name='logout')
]
