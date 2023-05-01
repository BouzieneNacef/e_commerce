
from rest_framework import serializers
from .models import *

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    #address = AddressSerializer(read_only = True)
    class Meta:
        model = Client
        fields = ('name','email', 'phone', 'typeClient')

class CommadSerializer(serializers.ModelSerializer):
    #client = ClientSerializer(read_only = True)
    #address = AddressSerializer(read_only = True)
    class Meta:
        model = Command
        fields = '__all__'

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


