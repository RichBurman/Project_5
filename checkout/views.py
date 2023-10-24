from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ShippingAddressForm
from cart.models import CartItem
from .models import Order
from django.contrib import messages

# Create your views here.


def checkout(request):
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            # Process the order
            # Get the user if authenticated
            user = request.user if request.user.is_authenticated else None
            cart_items = CartItem.objects.filter(user=user)
            total_price = 0

            for item in cart_items:
                if user and user.is_authenticated:
                    item_price = item.package.discounted_price
                else:
                    item_price = item.package.price

                total_price += item.quantity * item_price

            # Create the order
            shipping_address = form.cleaned_data['shipping_address']
            order = Order(user=user, total_price=total_price,
                          shipping_address=shipping_address)
            order.save()

            for item in cart_items:
                order.items.add(item)
                item.delete()

            messages.success(request, 'Your order has been placed successfully! We hope you enjoy your purchase!')
            return redirect('order_success')
        else:
            messages.error(
                request, 'Invalid shipping address. Please try again.')

    else:
        form = ShippingAddressForm()

    context = {'form': form}
    return render(request, 'checkout/checkout.html', context)
