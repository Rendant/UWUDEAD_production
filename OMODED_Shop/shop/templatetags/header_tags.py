from django import template
from shop.models import Collections

register = template.Library()


@register.simple_tag()
def get_collections():
    return Collections.objects.all()