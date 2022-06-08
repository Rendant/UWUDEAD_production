from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.decorators.cache import cache_page


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

    def get_context_data(self, **kwargs):
        context = super(Collection, self).get_context_data(**kwargs)
        context['collection_slug'] = self.kwargs['collection_slug']
        return context


class Good(DetailView):
    model = Goods
    template_name = 'shop/good_detail.html'
    context_object_name = 'good'
    slug_url_kwarg = 'good_slug'

    def get_queryset(self):
        category = self.kwargs.get('collection_slug', '')
        q = super().get_queryset()
        return q.filter(collection__slug=category)


class Search(ListView):
    model = Goods
    template_name = 'shop/search_list.html'
    context_object_name = 'found_goods'

    def get_queryset(self):
        url_parameter = self.request.GET.get('q')
        if url_parameter:
            return Goods.objects.filter(name__icontains=url_parameter)
        else:
            return None
