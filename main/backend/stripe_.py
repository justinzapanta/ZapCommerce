import stripe
from ..models import Products

stripe.api_key = 'sk_test_51P3HpARwnxAlG0woM5gi4tvcSMK87cIzSUq8OJHAY7acjz3lomsKI3HKfPC65RvVvhxLlJbEGXZoQ00FdM3NSJ7700I0AqZ1yd'

def create_stripe_product(product_info):
    for info in product_info:
        product = stripe.Product.create(
            name = info.product_name,
            description= info.product_details,
        )

        price = stripe.Price.create(
            currency = 'php',
            unit_amount = int(str(info.product_current_price) + '00'),
            product = product.id
        )

        update_product = Products.objects.filter(product_id = info.product_id).update(
            product_stripe_id = price.id,
            product_id_stripe = product.id
        )



def update_stripe_product(product):
    product_update  = stripe.Product.modify(
        product.product_id_stripe,
        name = product.product_name,
        description = product.product_details
    )

    new_price = stripe.Price.create(
        currency='php',
        unit_amount=int((str(int(product.product_current_price)) + '00')),
        product= product.product_id_stripe,
    )


    update = Products.objects.filter(product_id = product.product_id).update(
        product_stripe_id = new_price.id
    )