""" Defines URLs for photo_blog """
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "photo_blog"
urlpatterns = [
    # A landing page for photo_blog
    path("photo_blog/", views.photo_blog, name="photo_blog"),
    # A page for submitting a new blog article
    path("new_blog_article/", views.new_blog_article, name="new_blog_article"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
