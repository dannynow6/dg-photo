from django.shortcuts import render, redirect

# Main site page
def index(request):
    """The home page for dg_photography"""
    return render(request, "dg_photography/index.html")
