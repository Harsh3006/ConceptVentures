from django.urls import path
from . import views

urlpatterns = [
    path('<str:user_type>/basic-information', views.BasicInformation, name="basic-information"),
    path('transcriber/languages', views.TranscriberLanguageView, name="languages"),
    path('<str:user_type>/location', views.location, name="location"),
    path('vendor/agent-detail', views.agentDetail, name='agent-detail'),
    path('<str:user_type>/qualification', views.Qualification, name="qualification"),
    path('<str:user_type>/documents', views.documents, name="documents"),
    path('<str:user_type>/payment-details', views.PaymentDetail, name="payment-detail"),
]

