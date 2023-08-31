from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from rest_framework.filters import SearchFilter
from django.db.models import Q


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter, ]
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    # при необходимости добавьте параметры фильтрации
    def get_queryset(self):
        queryset = Stock.objects.all()
        products_id = self.request.query_params.get('products', None)
        search = self.request.query_params.get('search', None)
        if products_id is not None:
            queryset = queryset.filter(positions__product_id=products_id).distinct()
        if search is not None:
            queryset = queryset.filter(
                Q(positions__product__title__icontains=search) |
                Q(positions__product__description__icontains=search)
            ).distinct()
        return queryset

