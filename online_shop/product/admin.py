from django.contrib import admin
from product.models import Category, Discount, Product, OffCode
# Register your models here.


admin.site.register(Discount)
admin.site.register(OffCode)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name_en", "name_fa", "root")
    list_filter = ("root",)
    raw_id_fields = ("root",)
    ordering = ("name_en",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name_en", "name_fa", "brand_en", "brand_fa", "price", "category", "discount")
    list_filter = ("category", "brand_en")
    search_fields = ("name_en", "name_fa")
    ordering = ("name_en",)