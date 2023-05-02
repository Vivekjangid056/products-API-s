from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework import generics, mixins, status
from .models import Products
from django.http import Http404
from .serializers import ProductSerializer
from rest_framework.response import Response
from django.core.cache import cache


class productlist(APIView):
    # API view for non-primary key based operations to fetch and post data on the products model.
    
    def get(self, request):
        # Try to get products from cache
        products = cache.get('products') 
        # If the data is not in the cache, query the database and cache the results
        if not products:
            products= Products.objects.all()
            cache.set('products', products)
        serializer = ProductSerializer(products, many=True)
        # Return the data in JSON format.
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = ProductSerializer(data= request.data)
        if serializer.is_valid():
            # If a new product is created, delete the cached products list to reflect the changes.
            serializer.save()
            cache.delete('products')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class productdetails(APIView):
    # API view for primary key based operations to fetch, update, and delete individual products from the database.
    
    def get_object(self, pk):
        try:
            return Products.objects.get(pk = pk)
        except Products.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        # Try to get the product from cache
        product = cache.get(f'product_{pk}')
        if not product:
            # If the data is not in the cache, query the database and cache the results.
            product = self.get_object(pk)
            cache.set(f'product_{pk}', product)
        serializer = ProductSerializer(product)
        #Return the data in JSON format.
        
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data= request.data)
        if serializer.is_valid():
            # If a product is updated, delete its cached representation to reflect the changes.
            serializer.save()
            cache.delete(f'product_{pk}')
            cache.delete('products')
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        # Delete the cached product and product list to reflect the changes.
        cache.delete(f'product_{pk}')
        cache.delete('products')
        return Response(status=status.HTTP_204_NO_CONTENT)


''' using django generics to reduce the number of line of code

   # This class defines the view for fetching and creating a list of products.
class productlist(generics.ListCreateAPIView):
    # Fetch all the products from the database.
    queryset = Products.objects.all()
    # Use the ProductSerializer to serialize the data.
    serializer_class = ProductSerializer

# This class defines the view for retrieving, updating, and deleting a specific product.
class productdetails(generics.RetrieveUpdateDestroyAPIView):
    # Fetch all the products from the database.
    queryset = Products.objects.all()
    # Use the ProductSerializer to serialize the data.
    serializer_class = ProductSerializer'''


""" we can also use django mixins that is also an extended form of class based views
 mixins and generics are very helpful to perform "CRUD" based operations in a few lines of code
 in mixins we have in built class parameters that are as follows
 for creating objects                   =    mixins.CreateModelMixin
 for getiing the list of objects        =    mixins.ListModelMixin
 retrieveing the object based on the PK =    mixins.RetrieveModelMixin
 for updating a particular object on PK =    mixins.UpdateModelMixin
 for deleting an object based on PK     =    mixins.DestroyModelMixin
 """


"""class productlist(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    # View for listing and creating Products
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
       # Handle GET requests to retrieve a list of products
       
        return self.list(request)
    
    def post(self, request):

        # Handle POST requests to create a new product
        return self.create(request)

class productdetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

    #View for retrieving, updating and deleting a single Product

    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk):
        
        # Handle GET requests to retrieve a single product
        
        return self.retrieve(request, pk)
    
    def update(self, request, pk):
        
        # Handle PUT requests to update a single product
        
        return self.update(request, pk)
    
    def delete(self, request, pk):
        
        # Handle DELETE requests to delete a single product
        
        return self.destroy(request, pk)
     """
