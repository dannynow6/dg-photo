""" Defines URL patterns for dg_photography """

from django.urls import path
from . import views

app_name = "dg_photography"
urlpatterns = [
    # Home Page
    path("", views.index, name="index"),
    # A landing page for Dan G's Photography Website
    # path("dg_photos/", views.dg_photos, name="dg_photos"),
]
