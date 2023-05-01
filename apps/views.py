from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework import generics, mixins, status
from .models import Products
from django.http import Http404
from .serializers import ProductSerializer
from rest_framework.response import Response
from django.core.cache import cache


class productlist(APIView):
    """
    
    """
    def get(self, request):
        products = cache.get('products')
        if not products:
            products= Products.objects.all()
            cache.set('products', products)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete('products')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class productdetails(APIView):
    def get_object(self, pk):
        try:
            return Products.objects.get(pk = pk)
        except Products.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        product = cache.get(f'product_{pk}')
        if not product:
            product = self.get_object(pk)
            cache.set(f'product_{pk}', product)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data= request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete(f'product_{pk}')
            cache.delete('products')
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        cache.delete(f'product_{pk}')
        cache.delete('products')
        return Response(status=status.HTTP_204_NO_CONTENT)


'''# using django generics to reduce the number of line of code

class productlist(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class productdetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer'''



""" we can also use django mixins that is also extended form of class based views
 mixins and generics are very helpful to perform "CRUD" based operations in a few lines of code
 in mixins we have in built class parameters that are as follows
 for creating objects                   =    mixins.CreateModelMixin
 for getiing the list of objects        =    mixins.ListModelMixin
 retrieveing the object based on the PK =    mixins.RetrieveModelMixin
 for updating a particular object on PK =    mixins.UpdateModelMixin
 for deleting an object based on PK     =    mixins.DestroyModelMixin
 """


"""class productlist(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class productdetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def update(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)"""





        