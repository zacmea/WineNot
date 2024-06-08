from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from .serializers import WineSerializer, CollexnSerializer
from .models import Collexn, Wine

def collexn_list(request):
    if request.method == 'GET':
        collexns = Collexn.objects.all()
        serializer = CollexnSerializer(collexns, many=True)
        return JsonResponse(serializer.data, safe=False) # 'safe=False' allows for serialization of objects that are not dict-like

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        form = CollexnForm(request.data)
        if form.is_valid():
            collexn = form.save(commit=False)
            collexn.created_by = request.user
            collexn.save()

            serializer = CollexnSerializer(collexn)

            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'error': 'add somehting here later!...'})