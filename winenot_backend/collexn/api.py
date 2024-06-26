###Trying to implement the ability to remove a wine from a collection, here to line 68
# from django.http import JsonResponse
# from rest_framework.decorators import api_view
# from .models import Collexn, Wine
# from .serializers import CollexnSerializer, WineSerializer
# from .forms import CollexnForm
# from django.shortcuts import get_object_or_404

# @api_view(['GET'])
# def collexn_list(request):
#     collexns = Collexn.objects.all()
#     serializer = CollexnSerializer(collexns, many=True)
#     return JsonResponse(serializer.data, safe=False)  # 'safe=False' allows for serialization of objects that are not dict-like

# @api_view(['GET'])
# def collexn_detail(request, pk):
#     try:
#         collexn = Collexn.objects.get(pk=pk)
#     except Collexn.DoesNotExist:
#         return JsonResponse({'error': 'Collexn not found'}, status=404)
    
#     serializer = CollexnSerializer(collexn)
#     return JsonResponse(serializer.data, safe=False)

# @api_view(['POST'])
# def collexn_create(request):
#     data = request.data
#     data['created_by'] = request.user.id
    
#     # Collect wine data and create wine instances
#     wine_ids = []
#     for wine_data in data.get('wines', []):
#         new_wine = Wine.objects.create(**wine_data)
#         new_wine.save()
#         wine_ids.append(new_wine.id)
    
#     # Update the data to include wine IDs
#     data['wines'] = wine_ids
    
#     form = CollexnForm(data)
    
#     if form.is_valid():
#         collexn = form.save(commit=False)
#         collexn.created_by = request.user
#         collexn.wines.set(wine_ids)  # Associate the created wines with the collexn
#         collexn.save()
        
#         serializer = CollexnSerializer(collexn)
#         return JsonResponse(serializer.data, safe=False)
#     else:
#         print(form.errors)
#         return JsonResponse({'error': 'oops, form not valid'}, status=400)
    
# @api_view(['DELETE'])
# def collexn_delete(request, pk):
#     try:
#         collexn = Collexn.objects.get(pk=pk)
#         collexn.delete()
#         return JsonResponse({'message': 'Collection deleted successfully'}, status=204)
#     except Collexn.DoesNotExist:
#         return JsonResponse({'error': 'Collection not found'}, status=404)

# @api_view(['POST'])
# def remove_wine_from_collexn(request, pk, wine_id):
#     collexn = get_object_or_404(Collexn, pk=pk)
#     wine = get_object_or_404(Wine, id=id)
#     collexn.wines.remove(wine)
#     return JsonResponse({'status': 'success', 'message': 'Wine removed from collection'})

##What was working before I started trying to allow for the removal of a wine from a collection :
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Collexn, Wine
from .serializers import CollexnSerializer, WineSerializer
from .forms import CollexnForm

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
        collexn.wines.set(wine_ids)  # Associate the created wines with the collexn
        
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
    
# @api_view(['GET'])
# def remove_wine_from_collexn(request, pk, wine_id):
#     print(pk, wine_id)