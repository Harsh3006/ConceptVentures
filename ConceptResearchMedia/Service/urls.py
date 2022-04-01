from django.urls import path
from . import views
urlpatterns = [
    # Services Pages
    path('', views.service_home, name="crm-services"),
    path('market-research', views.market_research, name="market-research"),
    path('transcription', views.transcription, name="transcription"),
    # path('industry-report', views.industry_report, name="industry-report"),
    path('data-analytics', views.data_analytics, name="data-analytics"),
    # path('survey-creation', views.survey_creation, name="survey-creation"),
    path('panel-service', views.panel_service, name="panel-service"),
]
