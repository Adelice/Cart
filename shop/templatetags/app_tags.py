from django import template

register = template.Library()


@register.filter(name='cart_len')
def cart_length(value):
    c=value.__len__()
    print('hello')
    print(c)
    return c
