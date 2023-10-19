from django.shortcuts import render

# Create your views here.


def index(request):
    """ Return the index page """

    return render(request, 'home/index.html')


def about_us(request):
    return render(request, 'home/about_us.html')


def gallery(request):
    return render(request, 'home/gallery.html')


def reviews(request):
    return render(request, 'home/reviews.html')


def walking_packages(request):
    return render(request, 'home/walking_packages.html')
