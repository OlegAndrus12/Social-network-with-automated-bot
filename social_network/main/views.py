from django.shortcuts import render, redirect
from main.models import Post
from main.forms import CreatePostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "main/welcome.html")

@login_required
def feeds(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }
    return render(request, "main/feeds.html", context)

@login_required
def create_post(request):
    if request.method == "POST":
        create_post_form = CreatePostForm(request.POST)
        if create_post_form.is_valid():
            create_post_form.instance.user = request.user
            create_post_form.save()
        return redirect("/feeds")
    else:
        create_post_form = CreatePostForm()
    context = {
        'form' : create_post_form
    }
    return render(request, "main/create_post.html", context)