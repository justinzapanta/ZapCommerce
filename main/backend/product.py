from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Products, Product_star, User_review, Product_star, User_info
from django.core import serializers
from .stripe_ import create_stripe_product, update_stripe_product
import json

@csrf_exempt
def get_products(request, index, device):
    if request.method == 'GET':
        print('hello')
        limit = 10 * (index + 1)
        products = Products.objects.all()[index * 10 : limit]

        if device == 'mobile':
            limit = 6 * (index + 1)
            products = Products.objects.all()[index * 6 : limit]
        
        product_list = [
            {
                'product_id' : product.product_id,
                'product_image' : product.product_image.url,
                'product_name' : product.product_name,
                'product_price' : product.product_price,
                'product_discount' : product.product_discount
            }
            for product in products
        ]

        return JsonResponse({'products' : product_list}, status = 200)
    return JsonResponse({'message': 'error'}, status = 404)



@csrf_exempt
def seller_get_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data['id'])
        product = Products.objects.filter(product_id = data['id'])
        
        product_info = [
            {
                'product_name' : info.product_name,
                'product_price' : info.product_price,
                'product_discount' : info.product_discount,
                'product_rate' : info.product_rate,
                'product_details' : info.product_details,
                'product_price_w_disc' : info.product_current_price,
                'product_search_key' : info.product_search_key,
                'product_size' : info.product_size,
                'product_type' : info.product_type
            }

            for info in product
        ]

        return JsonResponse({'product' : product_info}, status = 200)
    return JsonResponse({'message': 'error'}, status = 404)


@csrf_exempt
def update_product(request):
    if request.method == 'POST':
        update_product = Products.objects.get(product_id = request.POST['product_id'])
        update_product.product_name = request.POST['product_name']
        update_product.product_price = request.POST['product_price']
        update_product.product_discount = request.POST['product_discount']
        update_product.product_details = request.POST['product_details']
        update_product.product_current_price = int(request.POST['product_price']) - ((int(request.POST['product_price']) / 100) * int(request.POST['product_discount']))
        update_product.product_search_key = request.POST['product_search_key']
        update_product.product_size = request.POST['product_size']
        update_product.product_type = request.POST['product_type']

        if request.FILES.get('product_image'):
            update_product.product_image = request.FILES['product_image']
            print('yess')

        update_product.save()


        update_stripe_product(update_product)

        return JsonResponse({'message' : 'success'}, status=200)
    return JsonResponse({'message' : 'error'}, status=404)


@csrf_exempt
def create_product(request):
    if request.method == 'POST':

        new_product = Products(
            product_name = request.POST['product_name'],
            product_price = int(request.POST['product_price']),
            product_discount = int(request.POST['product_discount']),
            product_current_price = int(request.POST['product_price']) - ( (int(request.POST['product_price']) / 100) * int(request.POST['product_discount']) ),
            product_details = request.POST['product_details'],
            product_search_key = request.POST['product_search_key'],
            product_size = request.POST['product_size'],
            product_image = request.FILES.get('product_image'),
            product_new_released = True,
            product_total_sale = 0,
            product_rate = 0,
        )

        new_product.save()
        
        product = Products.objects.filter(product_id = new_product.product_id)
        create_stripe_product(product)

        ratings = Product_star(product = new_product)
        ratings.save()
        
        return JsonResponse({'message' : 'success' })
    return JsonResponse({'message' : 'error' })


@csrf_exempt
def delete_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        delete_product = Products.objects.get(product_id = data['product_id']).delete()

        return JsonResponse({'message' : 'success'})
    return JsonResponse({'message' : 'error'})



@csrf_exempt
def product_rate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        rate = Products.objects.filter(product_id = data['product_id'])

        return JsonResponse({'product_rate' : rate[0].product_rate})
    return JsonResponse({'message' : 'error'})



@csrf_exempt
def submit_review(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = json.loads(request.body)
            
            #check if the user already review the product
            product = Products.objects.get(product_id = data['product_id'])
            user_info = User_info.objects.get(user_auth_credentials = request.user)

            reviewed = User_review.objects.filter(
                review_user = user_info, 
                review_product = product
            )
            
            if not reviewed:
                product.product_total_review = product.product_total_review + 1
                product.save()

                user_review = User_review(
                    review_product = product,
                    review_user = user_info,
                    review_comment = data['user_comment'],
                    review_rating = data['product_rating']
                )
                user_review.save()

                product_reviews = Product_star.objects.get(product = product)
                if data['product_rating'] == 5:
                    product_reviews.five_star_total = product_reviews.five_star_total + 1
                elif data['product_rating'] == 4:
                    product_reviews.four_star_total = product_reviews.four_star_total + 1
                elif data['product_rating'] == 3:
                    product_reviews.three_star_total = product_reviews.three_star_total + 1
                elif data['product_rating'] == 2:
                    product_reviews.two_star_total = product_reviews.two_star_total + 1
                elif data['product_rating'] == 1:
                    product_reviews.one_star_total = product_reviews.one_star_total + 1

                product_reviews.save()

                product_rate = (
                    5 * product_reviews.five_star_total +
                    4 * product_reviews.four_star_total +
                    3 * product_reviews.three_star_total +
                    2 * product_reviews.two_star_total +
                    1 * product_reviews.one_star_total
                ) / product.product_total_review
                

                product.product_rate = float(str(product_rate)[:4])
                product.save()
            else:
                product_reviews = Product_star.objects.get(product = product)
                if reviewed[0].review_rating == 5:
                    product_reviews.five_star_total = product_reviews.five_star_total - 1
                elif reviewed[0].review_rating == 4:
                    product_reviews.four_star_total = product_reviews.four_star_total - 1
                elif reviewed[0].review_rating == 3:
                    product_reviews.three_star_total = product_reviews.three_star_total - 1
                elif reviewed[0].review_rating == 2:
                    product_reviews.two_star_total = product_reviews.two_star_total - 1
                elif reviewed[0].review_rating == 1:
                    product_reviews.one_star_total = product_reviews.one_star_total - 1
                product_reviews.save()

                reviewed = User_review.objects.filter(
                    review_user = user_info, 
                    review_product = product
                ).update(
                    review_rating = data['product_rating'],
                    review_comment = data['user_comment']
                )

                product_reviews = Product_star.objects.get(product = product)
                if data['product_rating'] == 5:
                    product_reviews.five_star_total = product_reviews.five_star_total + 1
                elif data['product_rating'] == 4:
                    product_reviews.four_star_total = product_reviews.four_star_total + 1
                elif data['product_rating'] == 3:
                    product_reviews.three_star_total = product_reviews.three_star_total + 1
                elif data['product_rating'] == 2:
                    product_reviews.two_star_total = product_reviews.two_star_total + 1
                elif data['product_rating'] == 1:
                    product_reviews.one_star_total = product_reviews.one_star_total + 1
                product_reviews.save()

                product_rate = (
                    5 * product_reviews.five_star_total +
                    4 * product_reviews.four_star_total +
                    3 * product_reviews.three_star_total +
                    2 * product_reviews.two_star_total +
                    1 * product_reviews.one_star_total
                ) / product.product_total_review
                

                product.product_rate = float(str(product_rate)[:4])
                product.save()


            return JsonResponse({'message' : 'success'})
    return JsonResponse({'message' : 'error'})



@csrf_exempt
def check_user_review(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = json.loads(request.body)

            user_info = User_info.objects.get(user_auth_credentials = request.user)
            product_info = Products.objects.get(product_id = data['product_id'])

            user_review = User_review.objects.filter(
                review_user = user_info,
                review_product = product_info
            )

            if user_review:
                user_review_info = {
                    'rating' : user_review[0].review_rating,
                    'comment' : user_review[0].review_comment, 
                }
                
                return JsonResponse({'review' : user_review_info}, status=200)
            return JsonResponse({'review' : {}}, status=200)
    return JsonResponse({'message' : 'error'}, status=404)