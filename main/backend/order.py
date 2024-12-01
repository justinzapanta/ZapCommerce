from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from ..models import Transaction, Cart
import json


@csrf_exempt
def show_orders(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = json.loads(request.body)
            transaction = Transaction.objects.filter(
                transaction_invoice = data['invoice'],
                transaction_owner = request.user
                )

            item_list = [
                {
                    'product_id' : item.transaction_product.cart_product.product_id,
                    'product_image' : item.transaction_product.cart_product.product_image.url,
                    'product_qt' : item.transaction_product.cart_product_total_qt,
                    'product_name' : item.transaction_product.cart_product.product_name,
                    'product_size' : item.transaction_product.cart_product_size,
                    'product_price' : '{:,}'.format(item.transaction_product.cart_product.product_price),
                    'product_totalPrice' : '{:,}'.format(item.transaction_total_price),
                    'status' : item.transaction_status,
                }

                for item in transaction
            ]

            return JsonResponse({'items' : item_list}, status = 200)
    return JsonResponse({'message' : 'error' }, status = 404)



@csrf_exempt
def cancel_order(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = json.loads(request.body)
            
            update_order = Transaction.objects.filter(
                transaction_owner = request.user,
                transaction_invoice = data['invoice'],
                transaction_status = 'In Progress'
            ).update(
                transaction_status = 'Cancelled'
            )

        return JsonResponse({'message' : 'success'}, status = 200)
    return JsonResponse({'message' : 'error'}, status=404)


