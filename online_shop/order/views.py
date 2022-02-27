from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from order.serializer import OrderItemSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer