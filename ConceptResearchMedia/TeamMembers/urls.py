from django.urls import path
from .views import TeamMemberDetail
urlpatterns = [
    path('<slug:slug>', TeamMemberDetail.as_view(), name="member-detail")
]
