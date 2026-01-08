from django.urls import path
from .views import payment_process

urlpatterns = [
    path('process/<int:order_id>/', payment_process, name='payment_process'),
]
