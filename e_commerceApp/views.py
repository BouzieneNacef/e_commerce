from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max, Min
from .models import *
from .serializers import *

# Create your views here.

#define the Product CRUD using the ModelViewSet:
class ProductViewSet(viewsets.ModelViewSet):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        #the following line is to allow the http methods get,post,put,delete
        #it is not necessary because the default value is ['get','post','put','delete']
        #http_mettod_names =['get', 'post']

        #add  some custom methods to the viewset
        # detail = True: if the methode is applied a specific object
        # detail = False: if the methode is applied a list of object (all object)
        @action(methods=['get'], detail=False) 
        def max_min_price(self, request):
            if request.method!= 'GET':
                return Response({'message':'the method is not allowed', 'status':status.HTTP_405_METHOD_NOT_ALLOWED})
            #get the maximum and the minimum price:
            res = Product.objects.aggregate(Max('price'), Min('price'))
            #json ==> Response('key': value)
            #return Response({'max price ':res(0),'min price':res(1)})  
            #get the maximum price
            max_price = Product.objects.aggregate(Max('price'))['price__max']
            #get the minimum price
            min_price = Product.objects.aggregate(Min('price'))['price__min']
            # get the product with the maximum price:
            p_max = Product.objects.get(price=max_price)
            # get the product with the minimum price:
            p_min = Product.objects.get(price=min_price)
            # serializer p_max and p_min 
            serializer1 = ProductSerializer(p_max)
            serializer2 = ProductSerializer(p_min)
            # if the object is a list of object, we should use many = True
            # serializer = ProductSerializer(p_max, many= True)
            return Response({'Product with max price': serializer1, 'Product with min price': serializer2})

#define the Client CRUD using the ModelViewSet:        
class ClientViewSet(viewsets.ModelViewSet):
        queryset = Client.objects.all()
        serializer_class = ClientSerializer
        #the following line is to allow the http methods get,post,put,delete
        #it is not necessary because the default value is ['get','post','put','delete']
        #http_mettod_names =['get', 'post']

        #define a custom method to get the products of a client
        @action(methods=['get'],detail=True)
        def get_products(self,request,pk=None):
            #get the client
            client = Client.objects.get(id=pk)
            #get the products of the client
            products = client.products.all()
            #serialize the products
            serializer = ProductSerializer(products,many=True)
            #return the products
            return Response(serializer.data)
        #define a custom method to add a product to a client
        @action(methods=['post'],detail=True)
        #details=True because we are going to use the primary key of the client.
        #we would to perform the action on a single instance of client
        def command_product(self,request,pk=None):
            #get the client
            client = Client.objects.get(id=pk)
            #get the product
            product = Product.objects.get(id=request.data['product_id'])
            
            #add the product to the client
            client.client_products.add(product)
            #save the client
            client.save()
            #return the client
            return Response({'message':f'Command of product {product.label} by the client {client.name} was accepted'})
        #define a custom method to remove a product from a client
        @action(methods=['delete'],detail=True)
        def remove_product(self,request,pk=None):
            #get the client
            client = Client.objects.get(id=pk)
            #get the product
            product = Product.objects.get(id=request.data['product_id'])
            #remove the product from the client
            client.products.remove(product)
            #save the client
            client.save()
            #return the client
            return Response({'message':'Product removed from the client'})
        #define a custom method to perform more than one action
        @action(methods=['get','post'],detail=True)
        def products(self,request,pk=None):
            if request.method == 'GET':
                return self.get_products(request,pk)
            elif request.method == 'POST':
                return self.add_product(request,pk)

        #define a custom method to perform more than one action
        @action(methods=['get','post','delete'],detail=True)
        def products2(self,request,pk=None):
            if request.method == 'GET':
                return self.get_products(request,pk)
            elif request.method == 'POST':
                return self.add_product(request,pk)
            elif request.method == 'DELETE':
                return self.remove_product(request,pk)

#define the Provider CRUD using the ModelViewSet:
class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

#define the Command CRUD using the ModelViewSet:
class CommandViewSet(viewsets.ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommadSerializer    
    #define a custom method to get the products in stock ordered by a given client
    #The method should return products ordered by a given client in a period
    @action(detail=True, methods=['get'])
    def client_products(self, request, pk=None):
        client_id = request.query_params.get('client_id', None)
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)

        # if request parametres are not null 
        if client_id and start_date and end_date:
            try:
                client = Client.objects.get(pk=client_id)
                # strptime : to convert to string
                start_date = timezone.datetime.strptime(start_date, '%Y-%m-%d').date()
                end_date = timezone.datetime.strptime(end_date, '%Y-%m-%d').date()
            except (ValueError, Client.DoesNotExist):
                return Response(status=status.HTTP_400_BAD_REQUEST)
            # the commands of the client between the two dates
            commands = Command.objects.filter(client=client, date_cmd__range=[start_date, end_date])
            # create a list of products id
            product_ids = [command.product.id for command in commands]
            #  product in stock 
            products = Product.objects.filter(id__in=product_ids, stock__gt=0).order_by('label')

            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST)

#define the Address CRUD using the ModelViewSet:
class AddressViewSet(viewsets.ModelViewSet):
        queryset = Address.objects.all()
        serializer_class = AddressSerializer
