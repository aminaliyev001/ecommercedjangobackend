from django.db import models
from customers.models import Customer
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'new'),
        ('paid', 'paid'),
        ('shipped', 'shipped'),
        ('canceled', 'canceled'),
    ]
    customer   = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    status     = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    total      = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f"Order #{self.id}"

class OrderItem(models.Model):
    order      = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product    = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity   = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)