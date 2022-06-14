from django.contrib import admin
from .models import *


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'cost', 'is_available', 'is_clothes')
    filter_horizontal = ('collection', )
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_filter = ('collection',)
    prepopulated_fields = {"slug": ("name",)}


class CollectionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Collections, CollectionsAdmin)

