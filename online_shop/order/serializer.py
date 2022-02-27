from rest_framework import serializers
from order.models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    model = OrderItem
    fields = '__all__'