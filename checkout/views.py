from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# checkout view from code institute Boutique Ado


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LK18YLL987qhGQ332bSzdDbUgVQb4hcfZgVV4Z7uxqneNaF4JDh5ebVS7Zj3UAgQ9c0mNfNnyXDtX9NRxuJ7OiV00x5iIA8Uu',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
