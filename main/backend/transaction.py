from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from ..models import Cart, Transaction
import json


@csrf_exempt
def transaction_complete(request):
    if request.user.is_authenticated:
        current_date = datetime.now()
        formatted_date = current_date.strftime("%d/%m/%Y")

        cart_items = Cart.objects.filter(
            cart_owner = request.user,
            cart_checkout = False
        )

        try:
            transaction = Transaction.objects.all().order_by('-transaction_invoice')[0]
            invoice = transaction.transaction_invoice + 1
        except:
            invoice = 1

        total_price = 0
        for price in cart_items:
            total_price += price.cart_product_total_price

        total_item = len(cart_items)
        for item in cart_items:
            transaction_info = Transaction(
                transaction_product = item,
                transaction_total_price = total_price,
                transaction_owner = item.cart_owner,
                transaction_invoice = invoice,
                transaction_total_items = total_item,
                transaction_date  = formatted_date
            )

            transaction_info.save()

        cart_items.update(
            cart_checkout = True
        )

        return redirect('orders')
    return JsonResponse({'message' : 'error'}, staus = 404)