from django.shortcuts import *
from .models import *
# Create your views here.
from cart.forms import *
from cart.cart import Cart

from django.contrib.auth.decorators import login_required



@login_required(login_url='/accounts/login/')
def home(request):
    store = Store.get_all_store()  

    return render(request, 'index.html',{'store':store})
def single_store(request,store):
    # store=Store.object.get(id=id)
    # product=Product.object.filter(store_id=id).all()
    # products = Product.objects.filter(store_id=)
    
    print(store)

    selected_store = Store.objects.filter(id = store)

    products = Product.objects.filter(product_store = store).all()
    
    cat=Categories.objects.all()
  
    return render(request, 'home.html', {'cat':cat,'products':products ,' selected_store': selected_store })

# def index(request):
#     cat=Categories.objects.all()
    
#     return render(request,'home.html',{'cat':cat})

def product_category(request,n):
    all_prod=Categories.objects.get(slug=n)
    categories=Categories.objects.all()
    return render(request,'product_cat.html',{'cat':all_prod,'categories':categories})

def detail(request,d,slug):
    cart=Cart(request)
    #product=Product.objects.get(slug=slug)
    product = get_object_or_404(Product, id=d, slug=slug)
    if request.method=='POST':
        cartform=CartForm(request.POST)
        if cartform.is_valid():
            cd=cartform.cleaned_data
            cart.add(product=product,quantity=cd['quantity'],
                 update_quantity=cd['update'])

            return redirect('cart:cart_detail')

    else:
        cartform=CartForm()
        
    return render(request,'detail.html',{'prod':product,'cartform':cartform})
def article(request,id):
   articles = product.objects.get(pk = id)
   MyPaymentForm = Payment() 
   return render(request,"all-news/article.html", {"articles":articles, "MyPaymentForm":MyPaymentForm})
def search_results(request):

    if 'product_name' in request.GET and request.GET["product_name"]:
        search_term = request.GET.get("product_name")
        searched_products = Product.search_by_name(search_term)
        print(searched_products)
        store = None
        for item in searched_products:
            store=Store.objects.filter(store_name=search_term).all()
            print(store)
        
        for item in store:
            # print(item.product_store.product_name)
            message = f"{search_term}"
        return render(request, 'search.html',{"searched_products": searched_products})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message}) 