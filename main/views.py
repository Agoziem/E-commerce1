from django.shortcuts import render
from .models import *
from django.db.models import Max
from django.http import JsonResponse
import json
from books.models import Book
from .utils import cookieCart, cartData, guestOrder
from django.contrib.auth.decorators import login_required

def profile_view(request):
    data = cartData(request)
    order = data['order']
    context={
        "order":order,
    }
    return render(request,'profile.html',context)
    
@login_required(login_url='Accounts:login')
def cart_view(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    number_of_Items= len(items)
    context = {
        'items':items, 
        'order':order, 
        'cartItems':cartItems,
        'number_of_Items':number_of_Items,
        } 
    # max_price=Book.objects.aggregate(Max('price'))
    # # it will return a python Dict , then you find it and use it to rank the books
    # print(max_price)
    return render(request,'cart.html',context)




def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)
    
    customer = request.user.customer
    product = Book.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, status="Pending")
    orderItem, created = Orderitem.objects.get_or_create(customer_that_ordered=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    data={
        'num_of_cart':order.get_cart_items,
        'Total_Amount':order.get_cart_total,
        'item_Amount':orderItem.get_total,
        'item_quantity':orderItem.quantity
    }

    return JsonResponse(data,safe=False)

# deleting item from the Cart

def delete_item(request):
    data=json.loads(request.body)
    productId=data['productId']
    customer=request.user.customer
    book=Book.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer,status="Pending")
    orderitem,created=Orderitem.objects.get_or_create(customer_that_ordered=order,product=book)
    orderitem.delete()

    data={
        'num_of_cart':order.get_cart_items,
        'Total_Amount':order.get_cart_total
    }
    return JsonResponse(data,safe=False)


def review_item(request):
    data=json.loads(request.body)
    Customer_name=data['form']['name']
    productid=data['form']['productid']
    rating=data['form']['rating']
    comment=data['form']['comment']
    review,created=Product_review.objects.get_or_create(
        name=Customer_name,
        product_id=productid,
        comment=comment,
        rating=rating,
    )
    review.save()
    return JsonResponse(f'thanks {Customer_name} for your review, we really appreciate',safe=False)

def like_book(request):
    data=json.loads(request.body)
    Customer_name=data['form']['name']
    productid=data['form']['Book_id']
    checker=None
    review,created=Product_review.objects.get_or_create(name=Customer_name,product_id=productid)
    book=Book.objects.get(id=productid)
    print(review)
    if request.user.is_authenticated:
        if review.likes.filter(id=book.id).exists():
            review.likes.remove(book)
            checker=0
        else:
            review.likes.add(book)
            checker=1
    likes=review.likes.count()
    info={
        "check":checker,
        "likes":likes
    }
    return JsonResponse(info,safe=False)