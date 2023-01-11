from django.shortcuts import render, redirect
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
        form = PhotoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("dg_photography:index")

    context = {
        "form": form,
    }
    return render(request, "dg_photography/new_photo.html", context)
