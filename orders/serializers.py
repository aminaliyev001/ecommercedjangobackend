from rest_framework import serializers
from django.db import transaction
from decimal import Decimal

from .models import Order, OrderItem
from products.models import Product
from customers.models import Customer
from customers.serializers import CustomerSerializer
from products.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(source='product', queryset=Product.objects.all())
    product    = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product_id', 'quantity', 'unit_price', 'product']

class OrderSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(source='customer', queryset=Customer.objects.all())
    customer    = CustomerSerializer(read_only=True)
    items       = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'status', 'total', 'customer_id', 'customer', 'items']
        read_only_fields = ['id', 'created_at', 'total', 'customer']

    @transaction.atomic
    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        order = Order.objects.create(**validated_data)

        total = Decimal('0.00')
        for item in items_data:
            product = item['product']
            qty = item['quantity']
            price = item.get('unit_price', product.price)

            if product.stock < qty:
                raise serializers.ValidationError(
                    f"Not enough stock for product '{product.name}' (have {product.stock}, need {qty})."
                )

            OrderItem.objects.create(order=order, product=product, quantity=qty, unit_price=price)
            product.stock -= qty
            product.save(update_fields=['stock'])
            total += Decimal(str(price)) * Decimal(qty)

        order.total = total
        order.save(update_fields=['total'])
        return order

    def update(self, instance, validated_data):
        status = validated_data.get('status')
        if status:
            instance.status = status
            instance.save(update_fields=['status'])
        return instance