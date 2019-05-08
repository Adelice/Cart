from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Store(models.Model):
    store_pic = models.ImageField(upload_to='stores/', blank=True, verbose_name="logo/picture")
    store_name = models.CharField(max_length=30, verbose_name="store")
    store_location = models.CharField(max_length=30, verbose_name="location name")
    store_address = models.CharField(max_length=200, verbose_name="Address")
    store_city = models.CharField(max_length=30, verbose_name="city")
   
    # delivery_area = models.ManyToManyField(Zipcode)

    def __str__(self):
        return str(self.store_name) + " (" + str(self.store_location) + ")"

    class Meta:
        ordering = ['store_name','store_city', 'store_location']
    @classmethod
    def get_store_by_id(cls, id):
        store = cls.objects.get(pk=id)
        return store 
    @classmethod
    def get_all_store(cls):
        store= Store.objects.all()
        return store 

class Categories(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Categories)
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,null=True)
    #image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    pic = models.FileField(upload_to = 'pic',null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    product_store = models.ManyToManyField(Store, verbose_name="availability(ies) in store(s)")
    def __unicode__(self):
        return self.name
    @classmethod
    def search_by_name(cls,search_term):
        product = cls.objects.filter(name__icontains=search_term)
        return product    
    
