from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Collexn, Wine, CollexnWine
from .serializers import CollexnSerializer, WineSerializer
from .forms import CollexnForm
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def collexn_list(request):
    collexns = Collexn.objects.all()
    serializer = CollexnSerializer(collexns, many=True)
    return JsonResponse(serializer.data, safe=False)  # 'safe=False' allows for serialization of objects that are not dict-like

@api_view(['GET'])
def collexn_detail(request, pk):
    try:
        collexn = Collexn.objects.get(pk=pk)
    except Collexn.DoesNotExist:
        return JsonResponse({'error': 'Collexn not found'}, status=404)
    
    serializer = CollexnSerializer(collexn)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def collexn_create(request):
    data = request.data
    data['created_by'] = request.user.id
    
    # Collect wine data and create wine instances
    wine_ids = []
    for wine_data in data.get('wines', []):
        new_wine = Wine.objects.create(**wine_data)
        new_wine.save()
        wine_ids.append(new_wine.id)
    
    # Update the data to include wine IDs
    data['wines'] = wine_ids
    
    form = CollexnForm(data)
    
    if form.is_valid():
        collexn = form.save(commit=False)
        collexn.created_by = request.user
        collexn.save()

        # Associate the created wines with the collexn using the join table
        for wine_id in wine_ids:
            CollexnWine.objects.create(collexn=collexn, wine_id=wine_id)
        
        serializer = CollexnSerializer(collexn)
        return JsonResponse(serializer.data, safe=False)
    else:
        print(form.errors)
        return JsonResponse({'error': 'oops, form not valid'}, status=400)
    
@api_view(['DELETE'])
def collexn_delete(request, pk):
    try:
        collexn = Collexn.objects.get(pk=pk)
        collexn.delete()
        return JsonResponse({'message': 'Collection deleted successfully'}, status=204)
    except Collexn.DoesNotExist:
        return JsonResponse({'error': 'Collection not found'}, status=404)

@api_view(['POST'])
def remove_wine_from_collexn(request, pk, wine_id):
    collexn = get_object_or_404(Collexn, pk=pk)
    wine = get_object_or_404(Wine, pk=wine_id)
    CollexnWine.objects.filter(collexn=collexn, wine=wine).delete()
    return JsonResponse({'status': 'success', 'message': 'Wine removed from collection'})
