from rest_framework import serializers
from customer.models import Customer, Address
from django.urls import reverse


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
       # owner = HyperlinkedRelatedField(view_name='customer-detail', queryset=Customer.objects.all())
       # url = serializers.HyperlinkedIdentityField(view_name='address_api')