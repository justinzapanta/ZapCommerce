from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from ..models import Products, Cart

#cart
@csrf_exempt
def add_product(request):
    data = json.loads(request.body)
    product = Products.objects.filter(product_id = data['id'])
    
    exist_product = Cart.objects.filter(
        cart_product = product[0], 
        cart_owner = request.user, 
        cart_product_size = data['product_size'],
        )

    if not exist_product:
        cart = Cart(
            cart_checkout = False, 
            cart_product = product[0],
            cart_owner = request.user,
            cart_product_size = data['product_size'],
            cart_product_total_qt = 1,
            cart_product_total_price = product[0].product_price,
            cart_price = 0
            )
        cart.save()
        
        return JsonResponse({'message' : 'Added Successfully'}, status=200)
    return JsonResponse({'hello' : 'hi'}, status=200)

    
@csrf_exempt
def delete_product(request):
    data = json.loads(request.body)

    if data['id']:
        cart = Cart.objects.get(cart_id = data['id']).delete()
        return JsonResponse({'message' : 'success'}, status=200)
    return JsonResponse({'message' : 'error'}, status=200)


@csrf_exempt
def update_product(request):
    data = json.loads(request.body)

    if data['id']:
        cart = Cart.objects.filter(
            cart_id = data['id'],
            cart_owner = request.user,
            cart_checkout = False
            )

        price = int(cart[0].cart_product.product_price) * int(data['quantity'])
        update_cart = cart.update(
            cart_product_total_qt = data['quantity'],
            cart_product_total_price = price
            )
        
    return JsonResponse({'message' : 'hello'})


@csrf_exempt
def checkout(request):
    data = json.loads(request.body)

    cart = Cart.objects.filter(
        cart_owner = request.user,
        checkout = False
        )
    
    