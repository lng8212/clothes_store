from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Product
from ..serializers import *
from datetime import date
import json

@api_view(['GET'])
def getOrder(request):
    if(request.method == 'GET'):
        orders = ProductOrder.objects.all()
        serializers = ProductOrderSerializer(orders,many=True)
        return Response(serializers.data)

@api_view(['POST'])
def createOrder(request):
    if(request.method == 'POST'):
        serializer = CreateOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_order_data = serializer.validated_data
        
        # Map CreateOrder data to ProductOrder object
        product_order = ProductOrder(
            order_status='created',
            total_price=create_order_data['total_price'],
            user_id=create_order_data['user_id'],
            payment_method=create_order_data['payment_method'],
            order_date= date.today(),
        )
        product_order.save()

        # Add product IDs to ProductOrder using related model
        product_ids = create_order_data['product_ids']
        for x in product_ids:
            product_item = ProductItem.objects.get(id=x)
            product_item.order_id = product_order
            product_item.save()
            
        return Response({'status': 'success', 'order_id': product_order.id})
