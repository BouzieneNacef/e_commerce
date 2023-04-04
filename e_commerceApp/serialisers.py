from django.test import Client
from rest_framework import serializers
from .models import Product,Client

class PruductSerializer(serializers.ModelSerializer):
    class Mete:
        model = Product
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name','email', 'phone', 'typeClient')