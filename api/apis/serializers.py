#serializer data  to be rendered into json or xml format
from rest_framework import serializers

#Model importations
from .models import SuppliersModel


#Creation of serializer

class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    #model and fields declaration
    class Meta:
        model = SuppliersModel
        fields = '__all__'
