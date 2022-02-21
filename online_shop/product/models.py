from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from customer.models import Customer
# Create your models here.

class Category(BaseModel):
    """
    Category model contains details of categories
    """

    name_en = models.CharField(max_length=30, verbose_name=_("Category in english"),
    help_text=_("Please Enter category name in English"))

    name_fa = models.CharField(max_length=30, verbose_name=_("Category in persian"),
    help_text=_("Please Enter category name in Persian"))
    
    root = models.ForeignKey(to="self", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name_en
    


class AbstractDiscount(BaseModel):
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

    class Meta:
        abstract = True



class Discount(AbstractDiscount):
    
    def __str__(self):
        return f"{self.type}, {self.value}"
    



class OffCode(AbstractDiscount):
    """
    Off code is a code that makes a total discount on Order model
    """
    title = models.CharField(max_length=30, verbose_name=_("Disscount title"), help_text=_("What is this discount for?"))

    code = models.CharField(max_length=10, unique=True, verbose_name=_("Discount code"),
    help_text=_("Please Enter Off code"))
    
    


class Product(BaseModel):
    """
    Product model contains details of a product
    """

    name_en = models.CharField(max_length=30, verbose_name=_("Product name in english"),
    help_text=_("Please Enter product name in english"))

    name_fa = models.CharField(max_length=30, verbose_name=_("Product name in persian"),
    help_text=_("Please Enter product name in persian"))

    brand_en = models.CharField(max_length=30, verbose_name=_("Brand name in english"), 
    help_text=_("Please Enter brand name in english"))

    brand_fa = models.CharField(max_length=30, verbose_name=_("Brand name in persian"), 
    help_text=_("Please Enter brand name in persian"))

    price = models.FloatField(validators=[MinValueValidator(0)])

    image = models.ImageField(null=True, upload_to='static/images')

    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True)

    discount = models.ForeignKey(to=Discount, on_delete=models.SET_NULL, null=True, blank=True)


    @property
    def final_price(self):
        """
        This method calculates final price of a product by considering its discount
        """
        return self.price - profit_value(self.price)
        

    @property
    def raw_price(self):
        """
        This method just returns the price of product to be used in OrderItem method
        """
        return self.price

    
    def __str__(self):
        return self.name_en
    