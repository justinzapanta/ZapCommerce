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

    def __str__(self) -> str:
        return self.product_name
    

class Cart(models.Model):
    cart_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    cart_number = models.IntegerField(default= 1)
    cart_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart_product_size = models.CharField(max_length=100, null=True)
    cart_product_total_qt = models.IntegerField(null=True)
    cart_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_product_total_price = models.IntegerField(null=True)
    cart_date = models.CharField(max_length=50, null=True)
    cart_checkout = models.BooleanField(default=False)
    cart_price = models.IntegerField(null=True)


class Purchase(models.Model):
    purchase_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    purchase_cart_number = models.IntegerField()
    purchase_total_price = models.IntegerField()
