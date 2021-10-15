from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from main.models import Post, UserLike
from main.forms import CreatePostForm
from django.contrib.auth.decorators import login_required
import json

# Create your views here.
def index(request):
    return render(request, "main/welcome.html")

@login_required
def feeds(request):
    if request.method == "POST":
        if request.POST.get("operation") == "like_submit" and request.is_ajax():
            post_id=request.POST.get("post_id", None)
            post = get_object_or_404(Post, pk = post_id)
            if post.likes.filter(id=request.user.id): #already liked the content
                post.likes.remove(request.user) #remove user from likes 
                liked=False
            else:
                post.likes.add(request.user) 
                liked=True
            context = {"likes_count":post.total_likes,"liked":liked,"post_id":post_id}
            return HttpResponse(json.dumps(context), content_type='application/json')
    
    posts = Post.objects.all()
    already_liked=[]
    user_id = request.user.id
    for post in posts:
        if(post.likes.filter(id=user_id).exists()):
           already_liked.append(post.id)
    context = {"posts":posts,"already_liked":already_liked}
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