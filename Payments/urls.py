# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('make-payment/<int:reservation_id>/', views.make_payment, name='make_payment'),
    path('payment-success/', views.payment_success, name='payment_success')
]
