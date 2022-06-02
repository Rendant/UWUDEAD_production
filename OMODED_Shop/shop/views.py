from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, template_name='shop/mainPage.html')


def collections(request):
    return HttpResponse('<h1>Hello collections</h1>')


def collection(request, collection_slug):
    return HttpResponse('<h1>Hello collection</h1>')


def good(request, collection_slug, good_slug):
    return HttpResponse('<h1>Hello good</h1>')