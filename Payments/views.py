from django.shortcuts import render

# Create your views here.
# views.py

import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .form import PaymentForm
from armsApp.models import Reservation
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def make_payment(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    total_amount = reservation.calculate_total_amount()  # Implement this method in your Reservation model

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['stripeToken']
            try:
                charge = stripe.Charge.create(
                    amount=total_amount,
                    currency='usd',
                    description='Flight Booking Payment',
                    source=token,
                )

                # Payment successful
                reservation.status = 'paid'
                reservation.save()

                messages.success(request, 'Payment successful!')
                return redirect('payment_success')  # Redirect to payment success page
            except stripe.error.CardError as e:
                messages.error(request, f'Payment failed: {e.error.message}')
    else:
        form = PaymentForm()

    return render(request, 'payment.html', {'form': form})



def payment_success(request):
    # Render the payment success template
    return render(request, 'payment_success.html')
