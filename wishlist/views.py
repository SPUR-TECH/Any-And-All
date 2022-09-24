'''
Imports relevant django packages
'''
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product
from .models import Wishlist


@login_required
def view_wishlist(request):
    '''
    A view to return the wishlist
    '''
    wishlist = None
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        pass

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist.html', context)


@login_required
def add_to_wishlist(request, item_id):
    '''
    Add an item to the wishlist
    '''
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')

    wish, _ = Wishlist.objects.get_or_create(user=request.user)

    wish.products.add(product)
    messages.info(request, f'{product.name} was added to your wishlist')

    return redirect(redirect_url)


@login_required
def remove_from_wishlist(request, item_id):
    '''
    Removes the item from the wishlist
    '''
    wish = Wishlist.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=item_id)

    # Remove wish from the wishlist
    wish.products.remove(product)
    messages.info(request, f'{product.name} was removed from your wishlist')

    return redirect(reverse('wishlist'))
