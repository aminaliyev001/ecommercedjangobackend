from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    category_id   = serializers.PrimaryKeyRelatedField(
        source='category', queryset=Category.objects.all()
    )
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category_id', 'category_name']