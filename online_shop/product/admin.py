from django.contrib import admin
from product.models import Category, Discount, Product, OffCode
# Register your models here.


admin.site.register(Discount)
admin.site.register(OffCode)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("__all__")
    list_filter = ("root")
    raw_id_fields = ("name_en")
    ordering = ("name_en")

