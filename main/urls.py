from django.urls import path
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

    #product
    path('api/product/get-all/<int:index>/<str:device>', product.get_products),


    #transaction
    path('api/transaction/complete', transaction.transaction_complete),
    
    #my orders
    path('api/orders/show', order.show_orders),
    path('api/orders/cancel', order.cancel_order),


    #profile
    path('api/profile/update/password', profile.change_password),
    path('api/profile/verify/password', profile.check_user_password),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)