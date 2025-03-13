from django.urls import path
from .views import organization_view, home_page

app_name = "student"

urlpatterns = [

    path("organ/", organization_view, name="organ"),
    path("home/", home_page, name="home"),



]
