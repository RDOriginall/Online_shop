from django.contrib import admin
from order.models import OffCode, Order, OrderItem
# Register your models here.


admin.site.register(OffCode)
admin.site.register(Order)
admin.site.register(OrderItem)