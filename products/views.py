from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    search_fields = ['name', 'description'] 

    def get_queryset(self):
        qs = super().get_queryset()
        category_id = self.request.query_params.get('category_id')
        if category_id:
            qs = qs.filter(category_id=category_id)
        return qs