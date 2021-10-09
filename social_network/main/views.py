from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "main/welcome.html")

@login_required
def feeds(request):
    return render(request, "main/feeds.html")