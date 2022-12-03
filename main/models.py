from email.policy import default
from django.db import models
from books.models import Book
from django.contrib.auth.models import User


import secrets

class Customer(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE, null=True,blank=True)
	image=models.ImageField(upload_to='media', blank=True)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return str(self.name)

class Product_review(models.Model):
	name = models.CharField(max_length=200, null=True)
	product = models.ForeignKey(Book, on_delete= models.SET_NULL, null=True)
	comment=models.TextField( max_length=300, blank=True)
	rating=models.DecimalField(max_digits=4, decimal_places=2,null=True)
	likes=models.ManyToManyField(Book,related_name='likes')
	loves=models.ManyToManyField(Book,related_name='loves')
	date_reviewed = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return str(self.name)



# an Order is Our Cart whereas the Order Item is items within Our Cart
class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	customer = models.ForeignKey(Customer, on_delete= models.SET_NULL,blank=True, null=True,)
	date_ordered = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	ref=models.CharField(max_length=100, blank=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS ,default="Pending")

	def __str__(self):
		return str(self.customer)

	class Meta:
		ordering = ('-date_ordered',)
	

	@property
	def get_cart_total(self):
		orderitems=self.orderitem_set.all()
		total =sum([item.get_total for item in orderitems ])
		return total

	@property
	def get_cart_items(self):
		orderitems=self.orderitem_set.all()
		total =sum([item.quantity for item in orderitems ])
		return total

	@property
	def paystack_price(self):
		return self.get_cart_total*100

	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.Digital == False:
				shipping = True
		return shipping

class Orderitem(models.Model):
	product = models.ForeignKey(Book, on_delete= models.SET_NULL, null=True)
	customer_that_ordered = models.ForeignKey(Order, on_delete= models.SET_NULL, null=True)
	quantity= models.IntegerField(default=0,null=True,blank=True)
	date_added=models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total=self.quantity*self.product.main_Price
		return total


class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete= models.SET_NULL,blank=True, null=True,)
	order = models.ForeignKey(Order, on_delete= models.SET_NULL,blank=True, null=True,)
	address=models.CharField(max_length=200, null=True)
	city=models.CharField(max_length=200, null=True)
	state=models.CharField(max_length=200, null=True)
	Zipcode=models.CharField(max_length=200, null=True)
	date_added=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.address)
		
# debugging


class General_Customer_review(models.Model):
	image=models.ImageField(upload_to='media', blank=False,help_text = "upload your Face shot")
	name=models.CharField(max_length=300, null=True)
	comment=models.TextField( max_length=40, blank=True,help_text = "not exceeding 40 words")
	rating=models.DecimalField(max_digits=4, decimal_places=2)
	date_reviewed = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return str(self.name)
		
	@property
	def imageURL(self):
		try:
			url= self.image.url
		except:
			url=''
		return url

class Contact(models.Model):
	Name =models.CharField(max_length=100, blank=True, null=True)
	email = models.EmailField(blank=False,null=False)
	message=models.TextField(blank=False,null=False)
	date_sent= models.DateTimeField(auto_now_add=True, null=True, blank=True)
	
	def __str__(self):
		return str(self.Name)

class Subscription(models.Model):
	email = models.EmailField(blank=False,null=False)
	date_sent= models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return str(self.email)

