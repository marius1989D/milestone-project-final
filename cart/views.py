from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required()
def view_cart(request):
	"""
	Renders the cart content page
	"""
	return render(request, "cart/cart.html")

@login_required()
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = 1

    cart = request.session.get('cart', {})
    if id in cart:
        print(cart)
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('cart:view_cart'))

@login_required()
def adjust_cart(request, id):
    """
    Delete the Feature from the cart
    """
    
    
    cart = request.session.get('cart', {})

    cart.pop(str(id))

    request.session['cart'] = cart
    return redirect(reverse('cart:view_cart'))
