from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    product_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    product_image = models.ImageField(upload_to='./main/static/img/project_img', default=None, null=True)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_type = models.CharField(max_length=80)
    product_size = models.CharField(max_length=50)
    product_details = models.TextField()
    product_rate = models.FloatField()
    product_total_sale = models.IntegerField()
    product_new_released = models.BooleanField()
    product_discount = models.IntegerField()
    product_search_key = models.TextField()

    product_stripe_id = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.product_name
    

class Cart(models.Model):
    cart_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    cart_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart_product_size = models.CharField(max_length=100, null=True)
    cart_product_total_qt = models.IntegerField(null=True)
    cart_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_product_total_price = models.IntegerField(null=True)
    cart_checkout = models.BooleanField(default=False)
    cart_price = models.IntegerField(null=True)


class Transaction(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    transaction_product = models.ForeignKey(Cart, on_delete=models.CASCADE)
    transaction_status = models.CharField(max_length=100, default='In Progress')
    transaction_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_invoice = models.IntegerField(default=1)
    transaction_total_price = models.IntegerField()
    transaction_total_items = models.IntegerField()
    transaction_date = models.CharField(max_length=50)
    
    
    def __str__(self) -> str:
        return f'Invoice: {self.transaction_invoice} - {self.transaction_owner.username}'
