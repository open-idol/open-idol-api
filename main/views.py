from .serializers import *
from .models import *

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# class ItemViewSet(viewsets.ModelViewSet):
#     serializer_class = ItemSerializer
#     queryset = Item.objects.all()

@api_view(['GET'])
def get_or_create_items(request):
    if request.method == 'GET':
        serializer = ItemSerializer(Item.objects.all(), many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_article(request):
    if request.method == 'GET':
        serializer = ArticleSerializer(Article.objects.all(), many=True)

    return Response(serializer.data)
