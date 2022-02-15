from django.db import models
from core import BaseModel
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator

# Create your models here.

class Category(BaseModel):
    pass



class Product(BaseModel):
    """
    Product model contains details of a product
    """

    name = models.CharField(max_length=30, verbose_name=_("Product name"),
    help_text=_("Please Enter product name"))
    brand = models.CharField()
    price = models.FloatField(validators=[MinValueValidator(0)])
    image = models.imageFiels()
    category = models.ForeignKey(to=Category, on_delete=models.RESTRICT)
    discount = models.ForeignKey(to='Discount', on_delete=models.CASCADE)


    @property
    def final_price():
        pass


class Discount(models.Model):
    pass