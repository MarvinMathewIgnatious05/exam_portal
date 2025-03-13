
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages

# Create your views here.

User = get_user_model()

# User Registration View
def user_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        date_of_birth = request.POST.get('date_of_birth')
        phone = request.POST.get('phone_number')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        organization = request.POST.get('organization')
        profile_picture = request.FILES.get('profile_picture')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered")

            else:
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    email=email,
                    phone_number=phone,
                    address=address,
                    password=password,
                    date_of_birth=date_of_birth,
                    organization=organization,
                    profile_picture=profile_picture
                )
                user.save()
                messages.success(request, "Account created successfully! Please log in.")
                return redirect("authentication:user_login")
        else:
            messages.error(request, "Passwords do not match")

    return render(request, "user_registration.html")


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request,"successfully login")
            return redirect("")

        else:
            messages.error(request, "invalid username or password")
            print("invalid username or password")

    return render(request, "user_login.html")


def user_logout(request):
    logout(request)
    # print("successfully logout")


