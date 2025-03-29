from django.shortcuts import render
from .models import Order
from django.contrib.auth.decorators import login_required

@login_required
def checkout_view(request):
    orders = Order.objects.filter(user=request.user)
    total = sum(order.total_price() for order in orders)
    return render(request, 'checkout/checkout.html', {
        'orders': orders,
        'total': total
    })