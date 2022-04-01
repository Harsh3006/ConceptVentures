from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.CRMIndex, name="crm-index"),
    path('about', views.CRMAbout, name="crm-about"),
    path('contact', views.contact, name="contact"),
    path('work-with-us', views.work_with_us, name="work-with-us"),
    path('privacy-policy', views.PrivacyPloicy, name='privacy-policy'),

    path('user/', include('user.urls')),
    path('meet-our-team/', include('ConceptResearchMedia.TeamMembers.urls')),
    path('blog/', include('ConceptResearchMedia.Blog.urls')),
    path('case-study/', include('ConceptResearchMedia.CaseStudy.urls')),
    path('service/', include('ConceptResearchMedia.Service.urls')),
    path('account/', include('ConceptResearchMedia.Account.urls'))
]
