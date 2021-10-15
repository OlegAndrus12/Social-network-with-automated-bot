from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Post(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    likes = models.ManyToManyField(User, blank = "True", related_name = "likes", through="UserLike")

    @property
    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title

class UserLike(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    like_date = models.DateField(auto_now_add=True)