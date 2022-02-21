from django.contrib import admin
from product.models import Category, Discount, Product, OffCode
# Register your models here.


admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Product)
admin.site.register(OffCode)