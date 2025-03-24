from django.shortcuts import render
from .models import Organization
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="authentication:user_login")
def organization_view(request):
    orgns = Organization.objects.all()
    return render(request, "organization_view.html",{"orgn":orgns})

@login_required(login_url="authentication:user_login")
def main_page(request):
    return render(request, "main_page.html")

@login_required(login_url="authentication:user_login")
def home_page(request):
    return render(request, "home_page.html",)

def front_page(request):
    return render(request, "front_page.html")

