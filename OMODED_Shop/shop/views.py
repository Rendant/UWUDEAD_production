from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def index(request):
    collections = Collections.objects.all()
    context = {
        'collections': collections
    }
    return render(request, template_name='shop/mainPage.html', context=context)


def collections(request):
    return HttpResponse('<h1>Hello collections</h1>')


def collection(request, collection_slug):
    return HttpResponse('<h1>Hello collection</h1>')


def good(request, collection_slug, good_slug):
    return HttpResponse('<h1>Hello good</h1>')