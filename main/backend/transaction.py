from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from ..models import Cart, Transaction, Products, User_info
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



@csrf_exempt
def dashboard_info(request):
    date = json.loads(request.body)

    price_list = Transaction.objects.filter(transaction_date__endswith = date['year'], transaction_status = 'Delivered').exclude(transaction_status = 'Cancelled').values('transaction_invoice', 'transaction_total_price', 'transaction_date').distinct()
    total_product = Products.objects.count()
    total_users = User_info.objects.count()

    total_price = 0
    total_orders = 0
    for price in price_list:
        total_price += price['transaction_total_price']
        total_orders += 1

    year = date['year']
    month_yearList = [f'{month:02}/{year}' for month in range(1, 13)]
    sales_per_month = []

    for month_year in month_yearList:
        sales_list = Transaction.objects.filter(transaction_date__endswith = month_year, transaction_status= 'Delivered').exclude(transaction_status = 'Cancelled').values('transaction_invoice', 'transaction_total_price', 'transaction_date').distinct()
        total_sales = 0

        for sale in sales_list:
            if sale:
                total_sales += sale['transaction_total_price']
        
        sales_per_month.append(total_sales)

    print(total_orders)
    return JsonResponse({
        'total_price' : '{:,}'.format(total_price),
        'total_product' : total_product,
        'total_users' : total_users,
        'total_orders' : total_orders,
        'sales_per_month' : sales_per_month
        }, status=200)



@csrf_exempt
def update_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        transaction = Transaction.objects.filter(transaction_invoice = int(data['invoice'])).update(
            transaction_status = data['new_status']
        )
        
        print(transaction)
        return JsonResponse({'message' : "success"})
    return JsonResponse({'message' : "error"})
