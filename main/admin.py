from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Orderitem)
admin.site.register(General_Customer_review)
admin.site.register(Contact)
admin.site.register(Subscription)
admin.site.register(Product_review)

