from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Wishlist(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='wishlists')

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.id,
            'products': [product.id for product in self.products.all()],
        }

    def __str__(self):
        return f'Wishlist for {self.user.username}'
