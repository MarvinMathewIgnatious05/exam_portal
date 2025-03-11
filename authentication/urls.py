from django.urls import path
from .views import user_registration, user_login, user_logout

app_name = "authentication"

urlpatterns = [
    path("register/", user_registration, name="user_registration"),
    path("login/", user_login, name="user_login"),
    path("logout/", user_logout, name="user_logout"),

]
