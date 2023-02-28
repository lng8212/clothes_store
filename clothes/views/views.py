from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Product
from ..serializers import ProductSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def product(request):
    if(request.method == 'GET'):
        snippets = Product.objects.all()
        serializer = ProductSerializer(snippets, many = True)
        return Response(serializer.data)
    elif(request.method == 'POST'):
        serializer = ProductSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def productByCategory(request, category):
    if(request.method == "POST"):
        products = Product.objects.filter(category = category)
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
