from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import models

# Create your views here.
def store(request):
    new_product = models.Products.objects.filter(product_new_released = True)
    hot_deals = models.Products.objects.exclude(product_discount = 0).order_by('-product_discount')
    all_products = models.Products.objects.all()

    return render(request, 'main/views/store.html', 
                  {'mnew_released' : new_product[:6], 
                   'dnew_released' : new_product[:5] ,
                    'mhot_deals' : hot_deals[:6],
                    'dhot_deals' : hot_deals[:5],
                    'mall_product' : all_products[:6],
                    'dall_product' : all_products[:10]
                   })



def view_product(request, product_id):
    product = models.Products.objects.get(product_id = product_id)
    product_size = product.product_size.split(', ')
    product_price = '{:,}'.format(product.product_price)
    
    products = models.Products.objects.exclude(product_id = product_id).order_by('-product_total_sale')

    return render(request, 'main/views/view_product.html', {
        'product': product, 
        'product_size' : product_size, 
        'product_price' : product_price,
        'product_discount' : '{:,}'.format(int(product.product_price - ((product.product_price / 100) * product.product_discount))),
        'mproducts' : products[:6],
        'dproducts' : products[:10]
        })


def products(request, search = ''):
    products = models.Products.objects.filter(product_search_key__icontains = search.lower())[:20]
    result = search
    if search == 'deals':
        products = models.Products.objects.exclude(product_discount = 0).order_by('-product_discount')
        search = ''
    elif search == 'new-release':
        products = models.Products.objects.filter(product_new_released = True)
        search = ''
        result = 'New Release'
        
    return render(request, 'main/views/products.html', {
        'products' : products,
        'result' : result,
        'search' : search
    })



def sign_in(request, current_location='/'):
    data = {}

    if request.user.is_authenticated:
        return redirect('store')

    if request.method == 'POST':
        email = request.POST['email']
        user = authenticate(
            request,
            username=request.POST['email'],
            password=request.POST['password']
            )
        
        if user:
            login(request, user)

            return redirect(current_location)
        else:
            data['notif'] = 'Invalid Email or Password'
    return render(request, 'main/views/sign_in.html', data)



def sign_out(request):
    logout(request)
    return redirect('sign-in')



def sign_up(request):
    data = {}

    if request.user.is_authenticated:
        return redirect('store')
    
    if request.method == 'POST':
        email = request.POST['email']
        email_exist = User.objects.filter(username = email)

        if not email_exist:
            register_user = User.objects.create_user(
                username = email,
                password=request.POST['password']
            )
            register_user.save()

            user_info = models.User_info(user_auth_credentials = register_user)
            user_info.save()

            return redirect('sign-in')
        else:
            data['notif'] = 'Email already registered'

    return render(request, 'main/views/sign_up.html', data)



def cart(request):
    if request.user.is_authenticated:
        cart_products = models.Cart.objects.filter(cart_owner = request.user, cart_checkout = False)
        product_list = [
            {
                'cart_product' : product.cart_product,
                'cart_id' : product.cart_id,
                'cart_price' : '{:,}'.format(product.cart_price),
                'cart_product_total_price' : '{:,}'.format(product.cart_product_total_price),
                'cart_product_total_qt' : product.cart_product_total_qt,
                'product_price' : '{:,}'.format(product.cart_product.product_price ),
                'cart_product_size' : product.cart_product_size
            }

            for product in cart_products
        ]

        total_price = 0
        for price in cart_products:
            total_price += price.cart_product_total_price

        return render(request, 'main/views/cart.html', {'cart_products' : product_list, 'total_price' : '{:,}'.format(total_price)})
    return redirect('sign-in')


def order(request, status='all'):
    if request.user.is_authenticated:
        orders = models.Transaction.objects.filter(transaction_owner = request.user).order_by('-transaction_invoice').values('transaction_invoice').distinct()[:5]
        if status != 'all':
            orders = models.Transaction.objects.filter(transaction_owner = request.user, transaction_status = status ).order_by('-transaction_invoice').values('transaction_invoice').distinct()[:5]

        order_list = []
        try:
            current_invoice = orders[0]['transaction_invoice']
            for order in orders:
                if order['transaction_invoice'] == current_invoice:
                    item = models.Transaction.objects.filter(
                        transaction_owner = request.user,
                        transaction_invoice = order['transaction_invoice']
                    )
                    order_list.append(item[0])
                    current_invoice -= 1
        except:
            print('Error')

        return render(request, 'main/views/my_purchases.html', {'orders' : order_list, 'location' : status})
    return redirect('sign-in', current_location=request.path)


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = models.User_info.objects.get(user_auth_credentials = request.user)
            user.user_firstName = request.POST['first-name']
            user.user_lastName = request.POST['last-name']
            user.user_address = request.POST['address']
            user.save()
        
        user_info = models.User_info.objects.filter(user_auth_credentials = request.user)
        print(user_info)
        return render(request, 'main/views/profile.html', {'user_info' : user_info})
    else :
         return redirect('sign-in')