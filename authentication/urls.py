from django.urls import path
from .views import user_registration, user_login, user_logout, user_profile_view, user_profile_edit

app_name = "authentication"

urlpatterns = [
    path("register/", user_registration, name="user_registration"),
    path("login/", user_login, name="user_login"),
    path("logout/", user_logout, name="user_logout"),
    path("user_view/", user_profile_view, name="user_view"),
    path("user_edit/", user_profile_edit, name="user_edit"),
]
