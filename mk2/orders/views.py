from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Order

def order_create(request):
    if request.method == 'POST':
        order = Order.objects.create(
            first_name=request.POST['first_name'],
            email=request.POST['email'],
            address=request.POST['address'],
            city=request.POST['city']
        )

        # 📧 Customer confirmation email
        send_mail(
            subject='Order Confirmation',
            message=f'''
Hi {order.first_name},

Thank you for your order!
Your Order ID is: {order.id}

We will notify you once it is processed.
            ''',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[order.email],
            fail_silently=False,
        )

        # 📧 Store owner alert email
        send_mail(
            subject='🛒 New Order Received',
            message=f'''
New order received!

Order ID: {order.id}
Customer: {order.first_name}
Email: {order.email}
City: {order.city}

Please log in to the admin panel to process this order.
            ''',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.STORE_OWNER_EMAIL],
            fail_silently=False,
        )

        return redirect('payment_process', order_id=order.id)

    return render(request, 'orders/create.html')
