from django.shortcuts import render
from meta.views import Meta
def service_home(request):
    context={
        "meta": Meta(
                use_og=True,
                use_facebook=True,
                og_title='Experience the best service at CRM',
                description='At CRM, we help brands to connect with their audience across markets through key insights. We solve your business problems by putting together the best suited strategies with data, technology and human intelligence.',
                url='', 
                image='',
                object_type='website',
            )
    }
    return render(request, 'ConceptResearchMedia/services/services-home.html', context)

def market_research(request):
    context={
        "meta": Meta(
                use_og=True,
                use_facebook=True,
                og_title='Market Research at CRM',
                description='Whether you need to evaluate entry into a market, quickly test a new idea or optimize you messaging, our experienced team of quantitative researchers can help you reach the right groups and execute surveys that meet your research objectives on your timeline.',
                url='', 
                image='',
                object_type='website',
            )
    }
    return render(request, 'ConceptResearchMedia/services/market-research.html', context)

def transcription(request):
    context={
        "meta": Meta(
                use_og=True,
                use_facebook=True,
                og_title='Content Writing & Transcription services at CRM',
                description='CRM provides editorial services like proofreading , transcription, translation , content writing , data entry and annotations . get the highest quality of editorial support with CRM.',
                url='', 
                image='',
                object_type='website',
            )
    }
    return render(request, 'ConceptResearchMedia/services/transcription.html', context)

# def industry_report(request):
#     return render(request, 'services/industry-report.html')

def data_analytics(request):
    context={
        "meta": Meta(
                use_og=True,
                use_facebook=True,
                og_title='Data Analytics at CRM',
                description='Unleash the power of your data , generate transformative insights with our help , optimize processes , and enhance your ROI with CRM’s data analytics team.',
                url='', 
                image='',
                object_type='website',
            )
    }
    return render(request, 'ConceptResearchMedia/services/data-analytics.html', context)

# def survey_creation(request):
#     return render(request, 'services/survey-creation.html')

def panel_service(request):
    context={
        "meta": Meta(
                use_og=True,
                use_facebook=True,
                og_title='Data Analytics at CRM',
                description='Unleash the power of your data , generate transformative insights with our help , optimize processes , and enhance your ROI with CRM’s data analytics team.',
                url='', 
                image='',
                object_type='website',
            )
    }
    return render(request, 'ConceptResearchMedia/services/panel-service.html')