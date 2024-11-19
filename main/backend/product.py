from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Products
from django.core import serializers
import json

@csrf_exempt
def get_products(request, index, device):
    if request.method == 'GET':
        print('hello')
        limit = 10 * (index + 1)
        products = Products.objects.all()[index * 10 : limit]

        if device == 'mobile':
            limit = 6 * (index + 1)
            products = Products.objects.all()[index * 6 : limit]
        
        product_list = [
            {
                'product_id' : product.product_id,
                'product_image' : product.product_image.url,
                'product_name' : product.product_name,
                'product_price' : product.product_price,
                'product_discount' : product.product_discount
            }
            for product in products
        ]

        return JsonResponse({'products' : product_list}, status = 200)
    return JsonResponse({'Did you remember to set the method to GET in your fetch options?': 'hello'}, status = 404)