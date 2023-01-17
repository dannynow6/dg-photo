from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from .models import BlogArticle
from .forms import BlogArticleForm

# Create your views here


def photo_blog(request):
    """Basic landing page for Photo Blog Articles"""
    articles = BlogArticle.objects.order_by("date_published")
    context = {"articles": articles}
    return render(request, "photo_blog/photo_blog.html", context)

@login_required 
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


def article(request, article_id):
    """Show a single article's contents and info"""
    article = BlogArticle.objects.get(id=article_id)
    context = {"article": article}
    return render(request, "photo_blog/article.html", context)
