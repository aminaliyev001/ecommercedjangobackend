from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('customer').prefetch_related('items__product').all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        customer_id = self.request.query_params.get('customer_id')
        status = self.request.query_params.get('status')
        if customer_id:
            qs = qs.filter(customer_id=customer_id)
        if status:
            qs = qs.filter(status=status)
        return qs