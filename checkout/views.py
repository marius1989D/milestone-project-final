import stripe

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from features.models import Feature
from django.conf import settings
from django.utils import timezone


stripe.api_key = settings.STRIPE_SECRET


@login_required
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        
        
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Feature, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order = order, 
                    product = product, 
                    quantity = quantity
                    )
                order_line_item.save()
                
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "gbp",
                    source="tok_visa",
                    description = request.user.email,
                    
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('features:features_list'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        
        order_form = OrderForm()
        
    return render(request, "checkout/checkout.html", {'order_form': order_form, 'publishable': settings.STRIPE_PUBLISHABLE})
                