from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.FloatField() 
    totalQuantity = models.IntegerField()
    description = models.CharField(max_length=255)
    imageURL = models.CharField(max_length=255)

    def __str__(self):
       return self.product_name

class ProductOrder(models.Model):
    product_name = models.CharField(max_length=255)
    total_price = models.FloatField()
    user_id = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255)
    order_date = models.DateField()

    def __str__(self):
       return self.product_name

class Cart(models.Model):
    date = models.DateField(auto_now_add=True)
    def __str__(self):
       return self.date

class ProductItem(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_id = models.ForeignKey(ProductOrder, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
       return self.quantity
