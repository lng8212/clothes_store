from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Product
from ..serializers import ProductSerializer
# Create your views here.

@api_view(['GET'])
def product(request):
    if(request.method == 'GET'):
        snippets = Product.objects.all()
        serializer = ProductSerializer(snippets, many = True)
        return Response(serializer.data)
