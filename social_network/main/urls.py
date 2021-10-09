from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="welcome"),
    path("feeds/", views.feeds, name="feeds")
]
