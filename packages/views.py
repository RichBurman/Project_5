from django.shortcuts import render
from .models import Package

# Create your views here.


def package_list(request):
    packages = Package.objects.all()
    return render(request, 'package/package_list.html', {'packages': packages})