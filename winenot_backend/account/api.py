from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from .forms import SignupForm



@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
    })


@api_view(['POST'])
@authentication_classes([]) # This is necessary to allow unauthenticated requests to sign up for an account.
@permission_classes([]) # This is empty to allow unauthenticated requests to sign up for an account.
def signup(request):
    data = request.data
    message = 'success'

    form = SignupForm({
        'first_name': data.get('first_name'),
        'last_name': data.get('last_name'),
        'email': data.get('email'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })
    if form.is_valid():
        form.save()
    else:
        message = f"There was an error with your registration: {form.errors}"
        print (form.errors)

    return JsonResponse({'message': message})
