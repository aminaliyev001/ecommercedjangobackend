from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer
# ❌ remove: from .models import Order
# ✅ if you actually need Order here (usually you don't), do:
# from orders.models import Order

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    search_fields = ['full_name', 'email', 'phone']