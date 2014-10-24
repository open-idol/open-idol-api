from .models import *

from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
