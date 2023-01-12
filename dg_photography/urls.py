""" Defines URL patterns for dg_photography """
from django.conf import settings 
from django.conf.urls.static import static 
from django.urls import path
from . import views

app_name = "dg_photography"
urlpatterns = [
    # Home Page
    path("", views.index, name="index"),
    # New Photo Form 
    path("new_photo/", views.new_photo, name="new_photo"), 
    # A landing page for Dan G's Photography Website
    # path("dg_photos/", views.dg_photos, name="dg_photos"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
