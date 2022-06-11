from django.contrib import admin
from .models import *


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost', 'is_available',
                    'size_s', 'size_m', 'size_l', 'size_xl')
    filter_horizontal = ('collection', )
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_filter = ('collection',)
    prepopulated_fields = {"slug": ("name",)}


class GoodsNCAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost', 'is_available',
                    'quantity')
    filter_horizontal = ('collection', )
    search_fields = ('name', 'description')
    list_filter = ('collection',)
    prepopulated_fields = {"slug": ("name",)}


class CollectionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class StylesAdmin(admin.ModelAdmin):
    list_display = ('id', 'good_name')
    list_display_links = ('id', 'good_name')
    search_fields = ('good_name',)


admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsNC, GoodsNCAdmin)
admin.site.register(Collections, CollectionsAdmin)
admin.site.register(Styles, StylesAdmin)
