from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .backend import cart
from .backend import product

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
    

    #cart
    path('api/cart/add-product/', cart.add_product, name='add-product'),
    path('api/cart/delete-product', cart.delete_product, name='delete-product'),
    path('api/cart/update-product', cart.update_product, name='update-product'),
    path('api/cart/checkout', cart.checkout, name='checkout'),

    #product
    path('api/product/get-all/<int:index>/<str:device>', product.get_products),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)