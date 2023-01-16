from django.shortcuts import render, redirect
from .models import BlogArticle
from .forms import BlogArticleForm

# Create your views here


def photo_blog(request):
    """Basic landing page for Photo Blog Articles"""
    articles = BlogArticle.objects.order_by("id")
    context = {"articles": articles}
    return render(request, "photo_blog/photo_blog.html", context)


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
