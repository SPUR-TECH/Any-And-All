'''
Imports relevant django packages
'''
from django.contrib import admin
from .models import Product, Category, Review


class ProductAdmin(admin.ModelAdmin):
    '''
    Creates admin list display info
    '''
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'discount_price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    '''
    Creates admin list display
    '''
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    '''
    Creates admin list display info for reviews
    '''
    list_display = (
        'product',
        'review_writer',
        'created_on',
        'review',
        'rating',
    )


admin.site.register(Review, ReviewAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
