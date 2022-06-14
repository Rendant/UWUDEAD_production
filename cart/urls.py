from django.urls import path, re_path

from .views import (
    add_to_cart,
    delete_from_cart,
    order_details,
    # checkout,
    update_transaction_records,
    success
)

app_name = 'shopping_cart'


urlpatterns = [
    re_path(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    path('order-summary/', order_details, name="order_summary"),
    path('success/', success, name='purchase_success'),
    re_path(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    # path('checkout/', checkout, name='checkout'),
    re_path(r'^update-transaction/(?P<token>[-\w]+)/$', update_transaction_records, name='update_records')
]