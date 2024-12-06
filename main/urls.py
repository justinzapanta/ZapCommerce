from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .backend import product, transaction, cart, order, profile

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('products/', views.products, name='products'),
    path('products/<str:search>', views.products, name='products'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('view/<str:product_id>/', views.view_product, name='view_product'),
    path('view/<str:product_id>/<int:pagination>', views.view_product, name='view_product'),
    path('sign-in/<path:current_location>', views.sign_in, name='sign-in'),
    path('sign-out/', views.sign_out, name='sign-out'),
    path('orders/', views.order, name='orders'),
    path('orders/<str:status>', views.order, name='orders'),
    path('profile/', views.profile, name='profile'),

    #cart
    path('api/cart/add-product/', cart.add_product, name='add-product'),
    path('api/cart/delete-product', cart.delete_product, name='delete-product'),
    path('api/cart/update-product', cart.update_product, name='update-product'),
    path('api/cart/checkout', cart.checkout, name='checkout'),
    path('api/cart/total-item', cart.total_item),

    #product
    path('api/product/get-all/<int:index>/<str:device>', product.get_products),
    path('api/product/seller-product', product.seller_get_product),
    path('api/product/rate', product.product_rate),
    path('api/product/submit/review', product.submit_review),
    path('api/product/check/review', product.check_user_review),

    #transaction
    path('api/transaction/complete', transaction.transaction_complete),
    path('api/transaction/dashboard', transaction.dashboard_info),
    
    #my orders
    path('api/orders/show', order.show_orders),
    path('api/orders/cancel', order.cancel_order),

    #profile
    path('api/profile/update/password', profile.change_password),
    path('api/profile/verify/password', profile.check_user_password),


    #admin
    path('seller/', views.dashboard, name='dashboard'),
    path('seller/users', views.users, name='users'),
    path('seller/products', views.seller_products, name='seller-products'),
    path('api/seller/product/update', product.update_product),
    path('api/seller/product/new-product', product.create_product),
    path('api/seller/product/delete', product.delete_product),
    path('seller/orders', views.seller_orders, name='seller-orders'),
    path('seller/orders/<str:status>', views.seller_orders, name='seller-orders'),
    path('api/seller/orders/info', order.show_user_orders),
    path('api/seller/update/status', transaction.update_status),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)