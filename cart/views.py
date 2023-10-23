from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import CartItem
from packages.models import Package
from .forms import CartItemForm

User = get_user_model()

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = 0

    for item in cart_items:
        if request.user.is_authenticated:
            item_price = item.package.discounted_price
        else:
            item_price = item.package.price

        total_price += item.quantity * item_price

    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            cart_item = form.save(commit=False)
            if request.user.is_authenticated:
                cart_item.user = request.user
            cart_item.save()
            return redirect('cart:cart_view')
    else:
        form = CartItemForm()

    return render(request, 'cart/cart_view.html', {'cart_items': cart_items, 'total_price': total_price, 'form': form})