from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('collections/', collections, name='collections'),
    path('collections/<slug:collection_slug>/', collection,
         name='collection'),
    path('collections/<slug:collection_slug>/product/<slug:good_slug>',
         good, name='good')
]