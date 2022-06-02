from django.contrib import admin
from .models import *


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',
                    'cost')
    filter_horizontal = ('collection', )
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_filter = ('collection',)
    prepopulated_fields = {"slug": ("name",)}


class SizesAdmin(admin.ModelAdmin):
    list_display = ('id', 'good_name', 'size_s',
                    'size_m', 'size_l', 'size_xl')
    list_display_links = ('id', 'good_name')
    search_fields = ('good_name',)
    list_filter = ('size_s', 'size_m', 'size_l', 'size_xl')

class CollectionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Collections, CollectionsAdmin)
admin.site.register(Sizes, SizesAdmin)
