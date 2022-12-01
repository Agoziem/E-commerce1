from django.shortcuts import render
from main.models import *
from django.conf import settings
from main.utils import cookieCart, cartData, guestOrder
from django.http import JsonResponse
import json
import secrets

ref = secrets.token_urlsafe(20)

def checkout_view(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    number_of_Items= len(items)
    context = {
        'items':items, 
        'order':order, 
        'cartItems':cartItems,
        'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY,
        "number_of_Items":number_of_Items,
        
        }
    return render(request,'checkout.html',context)

def confirmation_view(request, id):
    order=Order.objects.get(id=id)
    items = order.orderitem_set.all()
    context={
        "order":order,
        "items":items
    }
    return render(request, 'payment-confirmation.html', context)
    
def processOrder(request):
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, status="Pending")
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    
    
    if total == order.get_cart_total:
        order.status = "Delivered"
        order.ref=ref
    order.save()
    
    if order.shipping == True:
        ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

    return JsonResponse("payment Successful", safe=False)