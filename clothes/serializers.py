from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','product_name', 'category', 'price', 'totalQuantity','description','imageURL')

    #product_name = models.CharField(max_length=255)
    # category = models.CharField(max_length=255)
    # price = models.FloatField() 
    # totalQuantity = models.IntegerField()
    # description = models.CharField(max_length=255)
    # imageURL = models.CharField(max_length=255)

class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ('id','order_status', 'total_price','user_id','payment_method', 'order_date')


    # product_name = models.CharField(max_length=255)
    # total_price = models.FloatField()
    # user_id = models.CharField(max_length=255)
    # payment_method = models.CharField(max_length=255)
    # order_date = models.DateField()

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id','date')

class ProductItemSerializer (serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = ('id','product_id', 'order_id','cart_id','quantity')

    # product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    # order_id = models.ForeignKey(ProductOrder, on_delete=models.CASCADE)
    # cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # quantity = models.FloatField()
    
class CreateOrderSerializer(serializers.Serializer):
    product_ids = serializers.ListField(child=serializers.IntegerField())
    user_id = serializers.CharField()
    payment_method = serializers.CharField()
    total_price = serializers.FloatField()
    
class GetCartSerializer(serializers.Serializer):
    product_item_id = serializers.IntegerField
    product_ids = serializers.ListField(child=serializers.IntegerField())
    user_id = serializers.CharField()
    payment_method = serializers.CharField()
    total_price = serializers.FloatField()