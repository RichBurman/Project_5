from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import CartItem
from packages.models import Package
from .forms import CartItemForm

User = get_user_model()


def calculate_item_price(user, item):
    if user.is_authenticated:
        return item.package.discounted_price
    return item.package.price


@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = 0

    for item in cart_items:
        item_price = calculate_item_price(request.user, item)
        total_price += item.quantity * item_price

    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            package_id = form.cleaned_data['package_id']
            quantity = form.cleaned_data['quantity']
            user = request.user
            existing_cart_item = CartItem.objects.filter(
                user=user, package_id=package_id).first()

            if existing_cart_item:
                existing_cart_item.quantity += quantity
                existing_cart_item.save()
                messages.success(
                    request, 'Item quantity updated successfully!')
            else:
                CartItem.objects.create(
                    user=user, package_id=package_id, quantity=quantity)
                messages.success(
                    request, 'Item added to the cart successfully!')
        else:
            messages.error(
                request, 'Invalid item or quantity. Please try again.')

    form = CartItemForm()
    return render(request, 'cart/cart_view.html', {'cart_items': cart_items, 'total_price': total_price, 'form': form})


def add_to_cart(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    user = request.user

    existing_cart_item = CartItem.objects.filter(
        user=user, package=package).first()

    if existing_cart_item:
        messages.info(request, 'Item is already in the cart.')
    else:
        CartItem.objects.create(user=user, package=package, quantity=1)
        messages.success(request, 'Item added to the cart successfully.')

    return redirect('cart:cart_view')
