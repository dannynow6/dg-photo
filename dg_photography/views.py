from django.shortcuts import render, redirect

# from django.contrib.auth.decorators import login_required
from .models import Photo
from .forms import PhotoForm

# Main site page
def index(request):
    """The home page for dg_photography"""
    return render(request, "dg_photography/index.html")


def new_photo(request):
    """New photo info submitted"""
    if request.method != "POST":
        form = PhotoForm()
    else:
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dg_photography:index")

    context = {
        "form": form,
    }
    return render(request, "dg_photography/new_photo.html", context)


def about(request):
    """dg photography about page"""
    photos = Photo.objects.order_by('year_taken')
    context = {'photos': photos}
    return render(request, "dg_photography/about.html", context)
