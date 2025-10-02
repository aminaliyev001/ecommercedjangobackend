from django.urls import path, include

urlpatterns = [
    path('api/categories/', include('categories.urls')),
    path('api/products/', include('products.urls')),
    path('api/customers/', include('customers.urls')),
    path('api/orders/', include('orders.urls')),
]