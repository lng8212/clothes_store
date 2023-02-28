from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Product
from ..serializers import *
import json

@api_view(['GET'])
def getCart(request):
    if(request.method == 'GET'):
        cart = Cart.objects.get(id=1)
        product_items = ProductItem.objects.filter(cart_id=cart.id)
        cart_items = []
        for product_item in product_items:
            product_serializer = ProductSerializer(product_item.product_id)
            item_serializer = ProductItemSerializer(product_item)
            cart_items.append({
                'product': product_serializer.data,
                'item': item_serializer.data,
            })
        
        return Response(cart_items)
    
@api_view(['POST'])
def addToCart(request):
    if(request.method == 'POST'):
       # parse the request body as JSON
        request_data = json.loads(request.body)
        
        # extract the product ID from the request data
        product_id = request_data.get('id')
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get(id=1)
        product_item = ProductItem.objects.create(product_id=product, cart_id=cart, quantity = 1)
        product_item.save()
        serializer = ProductItemSerializer(product_item)
        return Response(serializer.data)
    else:
        return Response({'error': 'Method not allowed'}, status=405)