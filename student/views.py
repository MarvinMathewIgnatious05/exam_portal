from django.shortcuts import render
from .models import Organization
# Create your views here.


def organization_view(request):
    orgns = Organization.objects.all()
    return render(request, "organization_view.html",{"orgn":orgns})

def main_page(request):
    return render(request, "main_page.html")

def home_page(request):
    return render(request, "home_page.html",)

def front_page(request):
    return render(request, "front_page.html")

