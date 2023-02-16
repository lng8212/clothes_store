from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Product
from ..serializers import *

@api_view(['GET'])
def getCart(request):
    if(request.method == 'GET'):
        snippets = Cart.objects.all()
        serializer = CartSerializer(snippets, many = True)
        return Response(serializer.data)