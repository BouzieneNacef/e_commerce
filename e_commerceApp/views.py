from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Client
from serializers import ProductSerializer, ClientSerializer

# Create your views here.

#product CRUD:
class ProductViewSet(viewsets.ModelViewSet):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        #the following line is to allow the http methods get,post,put,delete
        #it is not necessary because the default value is ['get','post','put','delete']
        http_mettod_names =['get', 'post']
        
class ClientViewSet(viewsets.ModelViewSet):
        queryset = Client.objects.all()
        serializer_class = ClientSerializer
        #the following line is to allow the http methods get,post,put,delete
        #it is not necessary because the default value is ['get','post','put','delete']
        http_mettod_names =['get', 'post']


