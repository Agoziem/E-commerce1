from django.shortcuts import render
from .models import *
from main.models import *
from itertools import groupby
from main.utils import cookieCart, cartData, guestOrder
from django.contrib.auth.decorators import login_required

@login_required(login_url='Accounts:login')
def books_view(request):
    data = cartData(request)
    order = data['order']
    books=Book.objects.all()
    newestbook=books.first()
    mainbooks=books.exclude(id=newestbook.id)
    category=BookCategory.objects.all()
    context={
        "order":order,
        "books":mainbooks,
        "newestbook":newestbook,
        "category":category,
    }
    return render(request,'Books.html',context)

@login_required(login_url='Accounts:login')
def Book_details(request,id):
    data = cartData(request)
    order = data['order']
    # best performing Book
    # mainreviews=Product_review.objects.order_by('product_id').values('name','comment','rating','product_id')
    # values=[
    #     {'product_id':k,'records':list(g)} for k,g in 
    #     groupby(mainreviews,lambda x : x['product_id'])
    #     ]
    mainreviews=Product_review.objects.all()   
    book=Book.objects.get(id=id)
    relatedreviews=book.product_review_set.all()
    features=book.bookfeatures_set.all()
    reviews=Product_review.objects.filter(product_id=book.id).aggregate(Avg('rating'))
    bookrating=reviews['rating__avg']
    print(book.likes)
    # top ranking Books excluding the featured book 
    related_books=Book.objects.filter(category=book.category.id).exclude(id=book.id)
    context={
        "order":order,
        'book':book,
        'bookrating':bookrating,
        'related_books':related_books,
        "features":features
    }
    return render(request,'book-details.html',context)