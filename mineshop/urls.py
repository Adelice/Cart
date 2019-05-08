
from django.conf.urls import url,include
from django.contrib import admin
from shop.views import *
from django.conf import settings
from django.contrib.auth import views 
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}),

    url(r'^$', home, name='home'),

    # url(r'^$',index,name='product_list'),
    url(r'^store/(\d+)', single_store, name='product_list'),
    url(r'^search/', search_results, name='search_results'),   
    url(r'cart/',include('cart.urls',namespace='cart')),
    url(r'^category/(\w+)/$',product_category,name='cate'),
    url(r'^detail/(\d+)/(\w+)/$',detail,name='detail')
]+ static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
