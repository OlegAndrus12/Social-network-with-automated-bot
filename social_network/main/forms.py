from django.forms import ModelForm
from main.models import Post

class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]
        exclude = ['user']
