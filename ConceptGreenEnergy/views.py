from django.shortcuts import render

# Create your views here.
def CGEIndex(request):
    return render(request, 'ConceptGreenEnergy/index.html')