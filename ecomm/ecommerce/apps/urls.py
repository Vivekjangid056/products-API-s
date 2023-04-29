from django.urls import path
from . import views

""" Here the first path simply indiacting to the "productlist class" in views file
 we kept the first path " ", blank for direct land on the productlist api view on browser
 
 In the second path we used the "productdetails<int:pk>" for jump on the details page 
  we have to add "productdetails" after 8000/ like http://127.0.0.1:8000/productdetails/ 
   after starting the server and for specific details we used primary key of the 
product that we will use after the productdetails/ 

  if we want to perform operations we have to simply write 
     http://127.0.0.1:8000/productdetails/1 
     
if we are using class based views in the views file then in the urls we have to add 
.as_view() function by convention"""


urlpatterns = [
    path("", views.productlist.as_view()),
    path("productdetails<int:pk>", views.productdetails.as_view())
]