from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    """
    A serializer for the Products model, to convert data to and from JSON format.
    """
    class Meta:
        model = Products
        fields = "__all__"
        """
        Specifies the model to use and the fields to include in the serialized output.
        In this case, all the fields of the Products model are included.
        """

