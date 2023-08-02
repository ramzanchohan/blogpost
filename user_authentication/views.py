from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from user_authentication.models import UserProfile
from django.contrib import messages


# Create your views here.

def signup(request):
    if request.method == 'POST':
        user_name = request.POST.get('uname')
        email = request.POST.get('email')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')

        if password != confirm_password:
            messages.error(request, "Your Password & Confirm Password are not same!")

        else:
            my_user = User.objects.create_user(user_name, email, password)
            my_user.first_name = first_name
            my_user.last_name = last_name
            my_user.save()
            return redirect('login')
        messages.success(request, 'Successfully Signup')

        # print(user_name, email, first_name, last_name, password, confirmp_assword)
    return render(request, 'blog/signup.html')


def userlogin(request):
    if request.method == 'POST':
        user_name = request.POST.get('uname')
        password = request.POST.get('password')
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, "blog/login.html")


def userlogout(request):
    logout(request)
    return render(request, 'blog/login.html')


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST' and request.FILES['img']:
        upload = request.FILES['img']
        print(upload)
        user = request.user
        instance = UserProfile.objects.get(user=user)
        instance.image = upload
        instance.save()

    return render(request, "blog/user_profile.html")


def change_password_view(request):
    if request.method == 'POST':
        new_password = request.POST.get('npassword')
        confirm_password = request.POST.get('confirm_password')
        if new_password != confirm_password:
            return HttpResponse("password doesn't match")

        # Perform any necessary validation (e.g., checking if old password is correct)

        # Update the user's password
        user = request.user
        user.set_password(new_password)
        user.save()
        # Optionally, you can redirect to a success page or display a success message
        return redirect('login')

    # If the form is not submitted or there is an error, render the form page again
    return render(request, 'blog/change_password.html')
