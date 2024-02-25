from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Category,Brand,Product
from .serializers import CategorySerializer,BrandSerializer,ProductSerializer

# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()
    # permission_classes = [IsAuthenticated]
    # serializer_class = CategorySerializer

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)

class BrandViewSet(viewsets.ViewSet):
    queryset = Brand.objects.all()

    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()

    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    @action(method=["get"],detail=False, url_path=r"category/(?P<slug>[\w-]+)",)
    def list_products_by_category(self, request, category=None):
        serializer = ProductSerializer(self.queryset.filter(category__name=category), many=True)
        return Response(serializer.data)


    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(
            self.queryset.filter(slug=slug),
            many=True
        )
        return Response(serializer.data)