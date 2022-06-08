from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='', default='')
    
    def __str__(self):
        return self.name
    
class Feature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.product) + ' Feature: ' + self.feature
    
class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()
    date_time = models.DateTimeField(default=now)
    
    def __str__(self):
        return str(self.customer) + ' Review: ' + self.content
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(default=now)
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orders.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orders.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=now)
    
    def __str__(self):
        return str(self.order)
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity        
        return total
    
class UpdateOrder(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    desc = models.CharField(max_length=1000)
    date = models.DateTimeField(default=now)
    
    def __str__(self):
        return str(self.order_id)
    
class CheckoutDetails(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    total_amount = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    payment = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(default = now)
    
    def __str__(self):
        return self.address
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    desc = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name    
    