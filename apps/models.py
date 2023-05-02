from django.db import models

class Products(models.Model):
    """
    A model representing a product for sale.
    """
    CATEGORY = (('cloths', 'CLOTHS'),
              ('grocery', 'GROCERY'),
              ('others', 'OTHERS')) 
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=10, choices=CATEGORY, default=None)

    def __str__(self):
        """
        Returns the name of the product as a string when the object is referenced.
        """
        return self.name
