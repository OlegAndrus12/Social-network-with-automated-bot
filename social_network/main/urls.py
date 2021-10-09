from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="welcome"),
    path("feeds/", views.feeds, name="feeds"),
    path("create/", views.create_post, name= "create_post")
]
