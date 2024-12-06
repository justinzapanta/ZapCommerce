from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import redirect
from django.contrib.auth.models import User
from ..models import User_info
import json


def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            if check_password(request.POST['current_passowrd'], request.user.password):
                user = User.objects.get(username = request.user.username)
                user.set_password(request.POST['new_password'])
                user.save()

        return redirect('sign-in')
    return redirect('sign-in')


@csrf_exempt
def check_user_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = json.loads(request.body)
            if check_password(data['current_password'], request.user.password):
                return JsonResponse({'message' : 'success'}, status=200)
            else:
                return JsonResponse({'message' : 'Invalid Password'}, status=200)
            
    return redirect('sign-in')


@csrf_exempt
def update_profiePicture(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.FILES.get('profile_picture'):

                user_profile = User_info.objects.get(user_auth_credentials = request.user)
                user_profile.user_profilePicture = request.FILES['profile_picture']
                user_profile.save()

            return JsonResponse({'message' : 'success'}, status=200)
    return JsonResponse({'message' : 'error'}, status=404)