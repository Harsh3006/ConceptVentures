from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import CaseStudy
from meta.views import Meta
# Create your views here.

class CaseStudyListView(ListView):
    model = CaseStudy
    template_name = 'ConceptResearchMedia/case-study/case-study-home.html'
    paginate_by = 10
    paginate_orphans = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meta"] = Meta(
                use_og=True,
                use_facebook=True,
                og_title='Case Study',
                description='Read our latest articles and reports, with expert perspectives, proprietary data, and thought-provoking insights.',
                url='', 
                image='',
                object_type='website')
        return context

class CaseStudyDetailView(DetailView):
    model = CaseStudy
    template_name = 'ConceptResearchMedia/case-study/customerStory.html'
    context_object_name = 'case_study'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_case_study"] = CaseStudy.get_related_case_study(self.object)
        return context
    