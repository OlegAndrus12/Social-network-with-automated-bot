from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        user_registration_form = RegisterForm(request.POST)
        if user_registration_form.is_valid():
            user_registration_form.save()
        return redirect("/feeds")
    else:
        user_registration_form = RegisterForm()
    
    context = {'form' : user_registration_form}
    return render(request, "register/register.html", context)

def login(request):
    return render(request, "register/login.html")