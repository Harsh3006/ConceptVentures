from django.urls import path
from .views import CaseStudyListView, CaseStudyDetailView

urlpatterns = [
    path('', CaseStudyListView.as_view(), name="case-study"),
    path('<slug:slug>', CaseStudyDetailView.as_view(), name="case-study-detail")
]
