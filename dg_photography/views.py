from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.decorators import login_required
from .models import Photo
from .forms import PhotoForm

# Main site page
def index(request):
    """The home page for dg_photography"""
    return render(request, "dg_photography/index.html")


@login_required
def new_photo(request):
    """New photo info submitted"""
    if request.method != "POST":
        form = PhotoForm()
    else:
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dg_photography:photos")

    context = {
        "form": form,
    }
    return render(request, "dg_photography/new_photo.html", context)


def about(request):
    """dg photography about page"""
    photos = Photo.objects.order_by("year_taken")
    context = {"photos": photos}
    return render(request, "dg_photography/about.html", context)


def photos(request):
    """dg photography page displaying photos uploaded to site"""
    photos = Photo.objects.order_by("year_taken")
    context = {"photos": photos}
    return render(request, "dg_photography/photos.html", context)


def photo(request, photo_id):
    """show a single photo and its details"""
    photo = Photo.objects.get(id=photo_id)
    context = {"photo": photo}
    return render(request, "dg_photography/photo.html", context)
