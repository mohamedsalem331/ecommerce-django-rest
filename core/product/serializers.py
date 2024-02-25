from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import Brand,Category,Product, ProductLine

class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields =  '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta():
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'


class ProductLineSerializer(serializers.ModelSerializer):
    product_image = ProductSerializer(many=True)

    class Meta:
        model = ProductLine
        fields = "__all__"
