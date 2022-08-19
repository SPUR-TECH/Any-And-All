# bab_tools from code institute Boutique Ado

from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


@register.filter(name='calculate_subtotal')
def calculate_subtotal(discount_price, quantity):
    return discount_price * quantity
