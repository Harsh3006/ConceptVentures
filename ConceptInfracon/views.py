from django.shortcuts import render

# Create your views here.
def CIIndex(request):
    return render(request, 'ConceptInfracon/index.html')