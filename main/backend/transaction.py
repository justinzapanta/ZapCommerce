from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from ..models import Cart, Transaction
import json


@csrf_exempt
def transaction_complete(request):
    cart_items = Cart.objects.filter(
        cart_owner = request.user,
        cart_checkout = False
    )

    try:
        transaction = Transaction.objects.all().order_by('-transaction_invoice')[0]
        invoice = transaction.transaction_invoice + 1
    except:
        invoice = 1

    for item in cart_items:
        transaction_info = Transaction(
            transaction_product = item,
            transaction_total_price = item.cart_product_total_price,
            transaction_owner = item.cart_owner,
            transaction_invoice = invoice
        )

        transaction_info.save()

    cart_items.update(
        cart_checkout = True
    )

    return redirect('cart')