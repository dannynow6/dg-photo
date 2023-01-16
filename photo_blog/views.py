from django.shortcuts import render

# Create your views here


def photo_blog(request):
    """Basic landing page for Photo Blog Articles"""
    return render(request, "photo_blog/photo_blog.html")
