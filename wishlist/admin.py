from django.contrib import admin
from .models import Wishlist, WishlistProduct

# Register your models here.
admin.site.register(Wishlist)
admin.site.register(WishlistProduct)