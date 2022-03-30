from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == "POST":
        user_registration_form = RegisterForm(request.POST)
        if user_registration_form.is_valid():
            user = user_registration_form.save()
            auth_login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("/feeds")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        user_registration_form = RegisterForm()
    
    context = {'form' : user_registration_form}
    return render(request, "register/register.html", context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/feeds")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
        form = AuthenticationForm()
        
        return render(request=request, template_name="register/login.html", context={"form":form})