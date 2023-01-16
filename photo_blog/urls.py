""" Defines URLs for photo_blog """

from django.urls import path
from . import views

app_name = "photo_blog"
urlpatterns = [
    # A landing page for photo_blog
    path("photo_blog/", views.photo_blog, name="photo_blog"),
]
