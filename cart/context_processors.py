from .cart import Cart

#make a variable available in all templates
def cart(request):
    return {'cart': Cart(request) }
