from django.shortcuts import render


# Create your views here.

def Home(request):
    return render, "index.html"

def rpds_app(request):
    return  render, "rpds.html"

def contact(request):
    return render, "contact.html"
