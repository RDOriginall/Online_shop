from django.db import models
from core import BaseModel
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator

# Create your models here.

class Category(BaseModel):
    """
    Category model contains details of categories
    """

    name = models.CharField(max_length=30, verbose_name=_("Category"),
    help_text=_("Please Enter category name"))
    root = models.ForeignKey(to="self", on_delete=models.CASCADE, null=True, blank=True)




class Discount(BaseModel):
    """
    Discount models decreases the price of a product
    """
    value = models.PositiveIntegerField()
    type = models.CharField(max_length=10, choices=[('price', 'Price'), ('percent', 'Percent')])
    max_price = models.PositiveIntegerField(null=True, blank=True)

    def profit_value(self, price:int):
        """
        profit method calculates and returns the profit of the discount
        """

        if self.type == 'price':
            return min(self.value, price)
        else: # percent
            raw_profit = int((self.value/100) * price)
            return int(min(raw_profit, int(self.max_price))) if self.max_price else raw_profit



class Product(BaseModel):
    """
    Product model contains details of a product
    """

    name = models.CharField(max_length=30, verbose_name=_("Product name"),
    help_text=_("Please Enter product name"))
    brand = models.CharField(max_length=30, verbose_name=_("Brand name"), 
    help_text=_("Please Enter brand name"))
    price = models.FloatField(validators=[MinValueValidator(0)])
    image = models.imageFiels()
    category = models.ForeignKey(to=Category, on_delete=models.RESTRICT)
    discount = models.ForeignKey(to='Discount', on_delete=models.CASCADE)


    @property
    def final_price():
        """
        This method calculates final price of a product by considering its discount
        """
        return self.price - profit_value(self.price)
        