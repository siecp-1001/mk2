import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from orders.models import Order

stripe.api_key = "YOUR_STRIPE_SECRET_KEY"

def payment_process(request, order_id):
    order = Order.objects.get(id=order_id)

    if request.method == 'POST':
        stripe.Charge.create(
            amount=5000,  # example amount in cents
            currency='usd',
            description=f'Order {order.id}',
            source=request.POST['stripeToken']
        )
        order.paid = True
        order.save()
        return redirect('payment_success')

    return render(request, 'payments/process.html', {'order': order})
