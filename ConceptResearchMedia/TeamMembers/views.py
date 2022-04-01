from django.shortcuts import render
from django.views.generic import DetailView
from .models import TeamMembers
    
class TeamMemberDetail(DetailView):
    model = TeamMembers
    template_name = 'ConceptResearchMedia/team-member/member-detail.html'
    context_object_name = 'member'