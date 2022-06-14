from django.urls import path, include
from .views import *
from accounts.views import my_profile

app_name = 'products'


urlpatterns = [
    path('', index, name='home'),
    path('collections/', CollectionsView.as_view(), name='collections'),
    path('search/', search, name='search'),
    path('collections/<slug:collection_slug>/', Collection.as_view(), name='collection'),
    path('collections/<slug:collection_slug>/product/<slug:good_slug>/', Good.as_view(), name='good'),
    path("account/register/", register_request, name="register"),
    path('account/login/', LoginRequest.as_view(), name='login'),
    path('account/password_reset/', ResetRequest.as_view(), name='password_reset'),
    path('account/profile/', my_profile, name='profile'),
    path('cart/', include('cart.urls')),
    path('pages/conventions_2022/', conventions, name='conventions'),
    path('pages/collaborations/', collaborations, name='collaborations'),
    path('pages/retailers/', retailers, name='retailers'),
    path('pages/about/', about, name='about'),
    path('community/faq/', faq, name='faq'),

]

urlpatterns += [
    path('account/', include('django.contrib.auth.urls')),
]