from django.shortcuts import render, redirect
from .models import BlogArticle
from .forms import BlogArticleForm

# Create your views here


def photo_blog(request):
    """Basic landing page for Photo Blog Articles"""
    return render(request, "photo_blog/photo_blog.html")


def new_blog_article(request):
    """New Blog Article Form"""
    if request.method != "POST":
        form = BlogArticleForm()
    else:
        form = BlogArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("photo_blog:photo_blog")
    context = {
        "form": form,
    }
    return render(request, "photo_blog/new_blog_article.html", context)
