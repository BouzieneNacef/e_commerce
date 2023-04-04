from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from serialisers import ClientSerializer

# Create your views here.

#product CRUD:
class ProductViewSet(viewsets.ModelViewSet):
    class Meta:
        queryset = Product.objects.all()
        serialzer_class = ClientSerializer
        http_mettod_names =['get', 'post']
        


