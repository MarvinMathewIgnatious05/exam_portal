from django.shortcuts import render
from .models import Organization
# Create your views here.


def organization_view(request):
    orgns = Organization.objects.all()
    return render(request,"organization_view.html",{"orgn":orgns})


def home_page(request):
    return render(request,"home_page.html",)

