#import external modules
from rest_framework import serializers

#import project modules
from .models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
