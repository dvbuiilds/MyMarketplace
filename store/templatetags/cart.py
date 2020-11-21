from django import template


register = template.Library()

@register.filter(name = 'is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        #print(id, product.id)
        #print(type(id), type(product.id))
        if int(id) == product.id:
            return True
        #print(keys)
    return False

@register.filter(name = 'cart_qt')
def cart_qt(product, cart):
    keys = cart.keys()
    for id in keys:
        #print(id, product.id)
        #print(type(id), type(product.id))
        if int(id) == product.id:
            return cart.get(id)
        #print(keys)
    return False

@register.filter(name='price_total')
def price_total(product, cart):
    return (product.price * cart_qt(product, cart))

@register.filter(name='total_cart_price')
def total_cart_price(products, cart):
    sum = 0
    for p in products:
        sum += price_total(p, cart)
    return sum

@register.filter(name='multiply')
def multiply(number, number1):
    return (number*number1)


