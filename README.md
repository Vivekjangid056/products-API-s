# products-API-s
CRUD API's for ecommerce products website

assignment = 

""" Goal:
          To deploy an API on PythonAnywhere with CRUD functionality
Task:
          You have to create a page using the following technologies
         - Python
         - MySQL
         - Django
         - Django Rest Framework
         - PythonAnywhere
         - Git
The code should be available on a public github repository.
Create a CRUD API for products of an ECommerce shopping website.
The code should be well documented and data should get saved in a MySQL database.
You will have to create a model in django consider the fields you can think of.
Host the code on PythonAnywhere so that it can be accessed via HTTP/HTTPS

Your code can have the following additions as well
          - Dockerising the application
          - Code is very well documented
          - API has documentation available
          - Fixtures for base data
          - Caching"""
          
          
          




SUMMARY OF THE CODE:

First of all go to command line and run the command
              django-admin startproject ecommerce
              cd .\ecommerce\
              python manage.py startapp app

// the first upper commande starts the project on django server that we can check by running command "python manage.py runserver"
// the second command creates an application where the files models.py, views.py is created with running the command

after running the upper three commands we have to configure the settings of our project

in the ecommerce directory we have settings.py file where we have section named "installed apps" we have to add "apps" that is our application and "rest_framework"
                INSTALLED_APPS = [
                        'django.contrib.admin',
                        'django.contrib.auth',
                        'django.contrib.contenttypes',
                        'django.contrib.sessions',
                        'django.contrib.messages',
                        'django.contrib.staticfiles',
                        'apps',
                        'rest_framework'
    ]
 After completing the this task we have databases section in the settings.py file. Here the default database is "sqlite3"
 we have to change the database from "sqlite3" to "mysql"
                      
                      DATABASES = {
                       'default': {
                       'ENGINE': 'django.db.backends.mysql',
                       'NAME': 'ecommerce',
                       'USER': 'root',
                       'PORT': '3305',
                       'PASSWORD': '#########'    #
    }
}

 These two things we have to do before write the code then move forward to the models.py file in app directory.
       Here we create the product class and define the attributes of the products
       the attributes will be store in the database tables in the form of columns.
       
 after models we have to create a file in the app level directory named serializers.py(any name).
 from rest_framework import serializer
 
 the serializer is used to serialize the data that we pass in json formate because the django models only accepts the data in the json formate.
 
 before applying the migrations we have to create our database in mysql 
                  open mysql workbench   and run the querries
                      CREATE DATABASE ecommerce;            # the database name should match to the name we write in the stiings.py file
                      USE ecommerce;
 
 now we can apply migrations
 
                  python manage.py makemigrations
                  python manage.py migrate
                  
after running the migrate command it will create some tables in the database.

the final thing is to create views and configure the urls.

I have used basic class based view and some advanced refined class based views that are provided by rest_framework 
                 
                 Basic classed based view
                 rest_framework.mixins
                 rest_framework.generics
                 
       created GET() and POST() method that are non primary key based functions
       
       GET(), PUT() and DELETE() method that are primary key based functions
       
      now create a file "urls.py" in app directory
      configure the urls
      
  now include the app/urls.py in urls.py file in ecommerce directory
  
                                         ## NOW THE API's ARE READY TO PERFORM OPERATIONS ##
     NOTE :
     
           the data should be given in this formate if generics or mixins are not in use because generics and mixins gives us extra functionality by creating a HTML form But the Basic class based views doesn't.
             
             {
    "id": 2,
    "name": "milk",
    "description": "tond milk",
    "price": "60.00",
    "quantity": 1,
    "category": "others"
}
                                         
      
      
      
      ## THIS IS HOW ALL THE BACKEND IS WORKING ##
      
 when we run the command "python manage.py runserver" 
    the server search for urls.py file in the project level directory where we have included the app level urls.py file 
    then it forwarded to app level urls.py and then it follows the path and it is redirected to views.py file and perform the 
    operations according to the functions we have defined in the views file.
                 


                  
            
 
 
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
