from django.shortcuts import render

from .models import Django, Python

# Create your views here.


def index(request):
    return render(request, "index.html", {})


def django(request):
    all_django = Django.objects.all()
    return render(request, "django.html", {
        "all_django": all_django
    })


def python(request):
    all_python = Python.objects.all()
    return render(request, "python.html", {
        "all_python": all_python
    })
