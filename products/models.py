from django.db import models
from categories.models import Category

class Product(models.Model):
    name        = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock       = models.PositiveIntegerField(default=0)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name