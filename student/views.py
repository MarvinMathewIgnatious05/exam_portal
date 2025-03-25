from django.shortcuts import render, redirect
from .models import Organization, Course
from django.contrib.auth.decorators import login_required
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



def view_Course_list(request):
    courses = Course.objects.all()
    return render(request, "view_course_list.html", {"course":courses})

def add_course(request):
    if request.method == "POST":
        course_name = request.POST.get("course_name")
        organization_id = request.POST.get("organization_id")
        description = request.POST.get("description")
        is_active = request.POST.get("is_active") == "on"


        organization = Organization.objects.get(id=organization_id)

        course = Course(course_name=course_name, organization=organization, description=description, is_active=is_active)
        course.save()

        return redirect("student:view_course")

    organizations = Organization.objects.all()
    return render(request,"add_course.html", {"organization": organizations})

