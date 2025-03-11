from django.urls import path
from .views import organization_view

app_name = "student"

urlpatterns = [
    path("organ/", organization_view, name="organ"),



]
