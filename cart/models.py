from __future__ import unicode_literals

from django.db import models

class PaymentForm(models.Model):
   fname = models.CharField(max_length = 100)
   lname = models.CharField(max_length = 100)
   email = models.CharField(max_length = 100)
   amount = models.CharField(max_length = 100)
   phonenumber = models.CharField(max_length = 100)
   transaction_code= models.IntegerField()