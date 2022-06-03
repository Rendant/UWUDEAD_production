from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views.generic import ListView


def index(request):
    return render(request, template_name='shop/mainPage.html')


class Collections(ListView):
    model = Collections
    template_name = 'shop/collections.html'


def collection(request, collection_slug):
    filtered_goods = Goods.objects.filter(collection__slug=collection_slug)
    context = {
        'filtered_goods': filtered_goods
    }
    return render(request, template_name='shop/collection.html', context=context)


def good(request, collection_slug, good_slug):
    return HttpResponse('<h1>Hello good</h1>')