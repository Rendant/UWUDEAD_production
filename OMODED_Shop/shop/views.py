from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views.generic import ListView, DetailView


def index(request):
    return render(request, template_name='shop/mainPage.html')


class Collections(ListView):
    model = Collections
    template_name = 'shop/collections_list.html'


class Collection(ListView):
    model = Goods
    template_name = 'shop/collection_list.html'
    context_object_name = 'filtered_goods'

    def get_queryset(self):
        return Goods.objects.filter(collection__slug=self.kwargs['collection_slug'])


class Good(DetailView):
    model = Goods
    template_name = 'shop/good_detail.html'
    context_object_name = 'good'

    def get_queryset(self):
        collection = self.kwargs.get('collection_slug', '')
        q = super().get_queryset()
        return q.filter(collection__slug=collection).select_related('collection')
# def good(request, collection_slug, good_slug):
#     return HttpResponse('<h1>Hello good</h1>')