from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel
# Create your models here.


class Customer(BaseModel):
    """
    customers only can see products, categories and make orders
    """

    # gonna compelete this model after learning about 'user' class

class Address(BaseModel):
    """
    Address model belongs to Customers and it contains Country, Province, City, Details and Postal code
    """

    customer = models.ForeignKey(to=Customer, on_delete=models.RESTRICT)

    country = models.CharField(max_length=30, default='Iran', verbose_name=_("country"),
    help_text=_("Please Enter your country(default: Iran)."))

    province = models.CharField(max_length=30, verbose_name=_("province"),
    help_text=_("Please Enter your province(Tehran, Shiraz, ...)"))

    city = models.CharField(max_length=30, verbose_name=_("city"))

    detail = models.CharField(max_length=255, verbose_name=_("address"), 
    help_text=_("Please Enter details of yout address(like street, allay and so on...)"))

    postal_code = models.CharField(max_length=10, unique=True, verbose_name=_("Zip code"), 
    help_text=_("Please Enter your zip code")) # needs validator !!!

    def __str__(self):
        return f"Country: {self.country}\nProvince: {self.province}\nCity: {self.city}\nAddress: {self.detail}\nPostal code: {self.postal_code}"
    