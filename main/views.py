import json

from .serializers import *
from .models import *

from django.db.models import Sum, Max

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
def get_article(request, item=None):
    if request.method == 'GET':
        item = Item.objects.get(name=item)
        # positive_article = Article.objects.filter(score__gt=0, item=item)
        # negative_article = Article.objects.filter(score__lt=0, item=item)
        #
        # positive_article = Article.objects.all().aggregate(Max('score'))

        articles = Article.objects.raw('''
            SELECT
                id, item_id, date, score,
                SUM(score > 0) as pos,
                SUM(score < 0) as neg
            FROM
                main_article
            WHERE
                item_id = %d
            GROUP BY
                date
        ''' % item.pk)

        result = {}
        result[item.name] = []
        for article in articles:
            result[item.name].append({
                'score': article.pos+article.neg,
                'pos': article.pos,
                'neg': article.neg,
                'date': str(article.date)
            })


        # serializer = ArticleSerializer(positive_article, many=True)

    return Response(json.dumps(result))
