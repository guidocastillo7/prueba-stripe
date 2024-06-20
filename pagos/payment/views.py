from django.shortcuts import render, redirect
import stripe 

# Create your views here.

stripe.api_key = 'mi-clave-prueba'

def create_checkout_session(request):

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items = [
                {
                    'price':'id-precio-prueba',
                    'quantity':1
                },
            ],
            mode = 'payment',
            success_url = 'http://localhost:8000/success',
            cancel_url = 'http://localhost:8000/cancel',
        )

    except Exception as e:
        return str(e)
    
    return redirect(checkout_session.url, code=303)


def checkout(request):
    return render(request, 'checkout.html')

def success(request):
    return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')