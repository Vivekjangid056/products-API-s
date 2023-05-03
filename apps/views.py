from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework import generics, mixins, status
from .models import Products
from django.http import Http404
from .serializers import ProductSerializer
from rest_framework.response import Response
from django.core.cache import cache


''' using django generics to reduce the number of line of code

   # This class defines the view for fetching and creating a list of products.'''
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
    serializer_class = ProductSerializer


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
