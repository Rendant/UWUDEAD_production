from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
from django.http import JsonResponse
from .forms import NewUserForm, LoginForm, ResetForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, template_name='shop/mainPage.html')


class CollectionsView(ListView):
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
        context.update({
            'collection_slug': self.kwargs['collection_slug'],
            'collection': Collections.objects.get(slug=self.kwargs['collection_slug']),
        })
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


def search(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        found_goods = Goods.objects.filter(name__icontains=url_parameter)
    else:
        found_goods = None

    ctx["found_goods"] = found_goods

    is_ajax_request = request.headers.get("x-requested-with") == "XMLHttpRequest"

    if is_ajax_request:
        html = render_to_string(
            template_name="inc/_search.html",
            context={"found_goods_ajax": found_goods}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, "shop/search_list.html", context=ctx)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            return render(request=request, template_name="registration/signup.html", context={"register_form": form})
    form = NewUserForm()
    return render(request=request, template_name="registration/signup.html", context={"register_form": form})


class LoginRequest(LoginView):
    form_class = LoginForm


class ResetRequest(PasswordResetView):
    form_class = ResetForm

