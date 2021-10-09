from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Post(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    likes = models.ManyToManyField(User, blank = "True", related_name = "likes")

    @property
    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
