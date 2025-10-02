from django.db import models

class Customer(models.Model):
    full_name = models.CharField(max_length=200)
    email     = models.EmailField(unique=True)
    phone     = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.full_name