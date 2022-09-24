'''
Imports relevant django packages
'''
from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Wishlist(models.Model):
    '''
    User wish list model
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="WishlistProduct")

    def __str__(self):
        return str(self.user)


class WishlistProduct(models.Model):
    '''
    Displays user wishlist details
    '''

    products = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(
        Wishlist, null=False, blank=False, on_delete=models.CASCADE)
