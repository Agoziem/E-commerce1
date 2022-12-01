from unicodedata import category
from django.shortcuts import render
from books.models import *
from main.models import *
from django.http import JsonResponse
import json
from main.utils import cookieCart, cartData, guestOrder
review_photos=[]
review_main_photos=[]
home_photos=[]
main_photos=[]
def home_view(request):
    data = cartData(request)
    order = data['order']
    books=Book.objects.all()
    newestbook=books.first()
    features=newestbook.bookfeatures_set.all()
    ShortBookscategory=BookCategory.objects.get(id=1)
    Novelscategory=BookCategory.objects.get(id=2)
    MainBookBookscategory=BookCategory.objects.get(id=3)
    books1=ShortBookscategory.book_set.all()
    books2=Novelscategory.book_set.all()
    books3=MainBookBookscategory.book_set.all()
    number1=len(books1)
    number2=len(books2)
    number3=len(books3)
    reviews=General_Customer_review.objects.all()
    review_list=reviews[:6]
    for review in reviews:
        review_photos.append(review.imageURL)
        review_main_photos=review_photos[:5]
    for book in books:
        home_photos.append(book.imageURL)
        main_photos=home_photos[:4]
    context={
        "newestbook":newestbook,
        "features":features,
        "number1":number1,
        "number2":number2,
        "number3":number3,
        "order":order,
        "bookimages":main_photos,
        "reviews":review_list,
        'review_main_photos':review_main_photos
    }
    return render(request,'home.html',context)


def submit_contact_form(request):
    data=json.loads(request.body)
    contactname=data['userformdata']['name']
    contactemail=data['userformdata']['email']
    contactmessage=data['userformdata']['message']
    contact_info=Contact.objects.create(
        Name=contactname,
        email=contactemail,
        message=contactmessage
    )
    contact_info.save()

    return JsonResponse('submitted successfully',safe=False)

def submit_sub_form(request):
    data=json.loads(request.body)
    subemail=data['userdata']['email']
    sub_email=Subscription.objects.create(email=subemail)
    sub_email.save()
    return JsonResponse('submitted successfully',safe=False)
