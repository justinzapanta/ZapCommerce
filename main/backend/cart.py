from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Products, Cart, User_info
from django.shortcuts import redirect
import json
import stripe

stripe.api_key = 'sk_test_51P3HpARwnxAlG0woM5gi4tvcSMK87cIzSUq8OJHAY7acjz3lomsKI3HKfPC65RvVvhxLlJbEGXZoQ00FdM3NSJ7700I0AqZ1yd'

#cart
@csrf_exempt
def add_product(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)
        product = Products.objects.filter(product_id = data['id'])
        
        exist_product = Cart.objects.filter(
            cart_product = product[0], 
            cart_owner = request.user, 
            cart_product_size = data['product_size'],
            cart_checkout = False,
            )

        if not exist_product:
            cart = Cart(
                cart_checkout = False, 
                cart_product = product[0],
                cart_owner = request.user,
                cart_product_size = data['product_size'],
                cart_product_total_qt = 1,
                cart_product_total_price = product[0].product_current_price,
                cart_price = 0
                )
            cart.save()
            
            return JsonResponse({'message' : 'Added Successfully'}, status=200)
        return JsonResponse({'message' : 'error'}, status=200)
    return redirect('sign-in')

    
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

        price = int(cart[0].cart_product.product_current_price) * int(data['quantity'])
        update_cart = cart.update(
            cart_product_total_qt = data['quantity'],
            cart_product_total_price = price
            )
        
    return JsonResponse({'message' : 'hello'})


@csrf_exempt
def checkout(request):
    link_url = ''
    user = User_info.objects.get(user_auth_credentials = request.user)
    if user.user_firstName == '' or user.user_address == '':
        link_url = '/profile'
    else:
        cart = Cart.objects.filter(
            cart_owner = request.user,
            cart_checkout = False
        )
        
        items = [
            {
                'price' : product.cart_product.product_stripe_id,
                'quantity' : product.cart_product_total_qt
            }
            for product in cart
        ]


        link = stripe.checkout.Session.create(
            line_items = items,
            mode = "payment",
            success_url = f"{request.scheme}://{request.get_host()}/api/transaction/complete",
            cancel_url = f"{request.scheme}://{request.get_host()}/cart",
        )
        
        link_url = link.url
    return JsonResponse({'link' : link_url}, status = 200)
    


@csrf_exempt
def total_item(request):
    if request.method == 'POST':
        total_product = Cart.objects.filter(cart_owner = request.user, cart_checkout = False).count()
        print(total_product)
        
        return JsonResponse({'count': total_product})
    return JsonResponse({'message': 'error'})
