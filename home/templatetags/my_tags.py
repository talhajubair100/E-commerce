from django import template
from order.models import ShopCart


register = template.Library()


@register.simple_tag
def my_cart_item(userid):
    cart_item = ShopCart.objects.filter(user_id=userid).count()
    return cart_item