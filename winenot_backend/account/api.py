from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from .forms import RegisterForm

@api_view(['POST'])
@permission_classes([]) # This is necessary to allow unauthenticated requests to sign up for an account.
@authentication_classes([]) # This is necessary to allow unauthenticated requests to sign up for an account.

def register(request):
    data = request.data
    message = f"Hello, {data['email']}! You have successfully registered."

    form = RegisterForm({
        'email': data['email'],
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'password1': data['password1'],
        'password2': data['password2'],
    })
    if form.is_valid():
        form.save()
    else:
        message = "There was an error with your registration."

    return JsonResponse({'message': message})
