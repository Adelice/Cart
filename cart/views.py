from django.shortcuts import *
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import *
from django.http import *
from django.core.urlresolvers import reverse
import requests
import random


# Create your views here.
@require_POST
def cart_add(request,product_id):
    cart= Cart(request)
    product = get_object_or_404(Product,id=product_id)
    form = CartForm(request.POST)
    if form.is_valid():
        cd=form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'],
                 update_quantity=cd['update'])
        
    return redirect('cart:cart_detail')   

def cart_remove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    #product = get_object_or_404(Product,id=d)

    for item in cart:
        
        item['update_quantity_form'] = CartForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    
    return render(request,'cart/detail.html',{'cart':cart})
    '''
    for item in cart:
        if item['product']==product:
            cart_product=item
    form = CartForm(initial={'quantity':cart_product['quantity'],
                             'update':True})
    return render(request,'cart/detail.html',{'cart_product':cart_product,
                                         'form':form,
                                         'product':product})
    '''
def article(request):
 
   MyPaymentForm = Payment() 
   return render(request,"all-news/article.html", {"MyPaymentForm":MyPaymentForm})
def SavePayment(request):
   saved = False
   data = {}
   hashed = random.randint(0,1000000)
   if request.method == "POST":
      #Get the posted form
      MyPaymentForm = Payment(request.POST, request.FILES)
      # print(MyPaymentForm.is_valid())
      if MyPaymentForm.is_valid():
         # workers = workers()
         payment = MyPaymentForm.save(commit=False)
         data['amount'] = payment.amount
         data['phonenumber'] = payment.phonenumber
         data['clienttime'] = '1556616823718'
         data['action'] = "deposit"
         data['appToken'] = "9563d7e60dc40e0315bc"
         data['hash'] = hashed
         payment.transaction_code = hashed
         # print(data)
         payment.save()
         print(payment.id)
         PaymentForm.objects.filter(id=payment.id).first()
         payload = data
         url = "https://uplus.rw/bridge/"
         requests.post(url, data=payload)
         return render(request,'cart/detail.html')
