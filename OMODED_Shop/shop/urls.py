from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('collections/', Collections.as_view(), name='collections'),
    path('search/', search, name='search'),
    path('collections/<slug:collection_slug>/', Collection.as_view(), name='collection'),
    path('collections/<slug:collection_slug>/product/<slug:good_slug>/', Good.as_view(), name='good'),
    path("account/register/", register_request, name="register"),
]

urlpatterns += [
    path('account/', include('django.contrib.auth.urls')),
]