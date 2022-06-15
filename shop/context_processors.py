from django.shortcuts import get_object_or_404
from accounts.models import Profile
from cart.models import Order
from django.contrib.auth import get_user_model


def cart_processor(request):
    if request.user.is_authenticated:
        user_profile = get_object_or_404(Profile, user=request.user)
        cart_orders = Order.objects.filter(owner=user_profile, is_ordered=False)
        return {'cart_orders': cart_orders}
    return {}
