# Category and Product models from code institute Boutique Ado

'''
Imports relevant django packages
'''
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    '''
    Category information
    '''
    class Meta:
        '''
        Changes category title to plural (categories)
        '''
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        '''
        Returns the category friendly name
        '''
        return self.friendly_name


class Product(models.Model):
    '''
    Product information
    '''
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        '''
        Returns the product name
        '''
        return self.name


class Review(models.Model):
    '''
    Review model
    '''
    review = models.TextField()
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True)
    product = models.ForeignKey(
        'Product', null=True, blank=True, on_delete=models.SET_NULL)
    review_writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''
        Returns the review as a string
        '''
        return f'{self.review}'
