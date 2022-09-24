'''
Imports relevant django packages
'''
from django.contrib import admin
from .models import Wishlist, WishlistProduct


admin.site.register(Wishlist)
admin.site.register(WishlistProduct)
