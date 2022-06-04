from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('collections/', Collections.as_view(), name='collections'),
    path('collections/<slug:collection_slug>/', Collection.as_view(), name='collection'),
    path('collections/<slug:collection_slug>/product/<slug:good_slug>/', Good.as_view(), name='good')
]