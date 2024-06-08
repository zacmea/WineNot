from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from .serializers import WineSerializer, CollexnSerializer

def collexn_list(request):
    if request.method == 'GET':
        collexns = Collexn.objects.all()
        serializer = CollexnSerializer(collexns, many=True)
        return JsonResponse({'data': serializer.data})

    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = CollexnSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)
    