from django import template


register = template.Library()

@register.filter(name = 'currency')
def currency(number):
    return '₹ '+str(number)

@register.filter(name = 'multiply1')
def multiply1(price):
    return (price * 0.2)