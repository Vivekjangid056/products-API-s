from django.db import models

# Create your models here.
class Products(models.Model):

    CATEGORY = (('cloths', 'CLOTHS'),
              ('grocery', 'GROCERY'),
              ('others', 'OTHERS')) 
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=10, choices= CATEGORY, default= None)
    def __str__(self):
        return self.name
