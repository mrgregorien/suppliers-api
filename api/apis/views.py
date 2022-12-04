from django.shortcuts import render

from rest_framework import viewsets


#importing local data
from .serializers import SupplierSerializer
from .models import SuppliersModels


# Create your views here.
class SuppliersViewSet(viewsets.ModelViewSet):
    #queryset defining
    queryset = SuppliersModels.objects.all()
    
    #specifying th serializer to be used
    serializer_class = SupplierSerializer
