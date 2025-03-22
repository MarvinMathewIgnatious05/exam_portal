from django.urls import path
from .views import organization_view, home_page, main_page, front_page

app_name = "student"

urlpatterns = [

    path("organ/", organization_view, name="organ"),
    path("home/", home_page, name="home"),
    path("main/", main_page, name="main"),
    path("front/", front_page, name="front"),

]
