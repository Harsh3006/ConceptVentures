from django.shortcuts import render, redirect

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject'] 
        message = request.POST['message']
        return redirect('/#contact')
    else:
        return render(request, 'ConceptVenture/index.html')
