from django.db import models
from django.db.models import Avg,Min,Max,Count,Q

class BookCategory(models.Model):
    cart=models.CharField(max_length= 300, blank=True)

    def __str__(self):
        return str(self.cart)

class Book(models.Model):
    title=models.CharField(max_length= 300, blank=True)
    Author=models.CharField(max_length= 300, blank=True)
    short_description=models.TextField(max_length=400, blank=True)
    long_description=models.TextField( blank=True)
    Ebookimage=models.ImageField(upload_to='media', blank=True)
    Ebook=models.FileField(upload_to='media', blank=True)
    price = models.FloatField(null=True)
    discount = models.FloatField(null=True)
    category = models.ForeignKey(BookCategory,null=True , on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    Digital=models.BooleanField(default=True,blank=False,null=False)
    Password=models.CharField(max_length= 300, blank=True)

    def __str__(self):
        return str(self.title)

    @property
    def rating(self):
        try:
            rating = self.product_review_set.aggregate(Avg('rating'))['rating__avg']
        except:
            rating= "no review yet"
        return rating

    @property
    def likes_count(self):
        likes = self.likes.count()
        return likes

    @property
    def main_Price(self):
        price=self.price
        discount=self.discount
        discounted_price=price*(discount/100)
        original_price=price-discounted_price
        return original_price


# using @ property helps us to perform some functions or manipulations on the Models fields
# and render it as an attribute instead of a Method

    @property
    def imageURL(self):
        try:
            url= self.Ebookimage.url
        except:
            url=''
        return url


class Bookfeatures(models.Model):
    book=models.ManyToManyField(Book)
    feature=models.CharField(max_length= 300, blank=True)
    def __str__(self):
        return str(self.feature)

class BookChapters(models.Model):
    book=models.ForeignKey(Book,null=True , on_delete=models.CASCADE)
    chapter_no=models.IntegerField(blank=True)
    Chapter_title=models.CharField(max_length= 300, blank=True)

    def __str__(self):
        return str(self.product)
