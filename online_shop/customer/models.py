from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel, User
from core.validators import Validators
from django.core.exceptions import ValidationError
# Create your models here.


class Customer(models.Model):
    """
    customers only can see products, categories and make orders
    """

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=30, verbose_name=_("First Name"), help_text=_("Please Enter your first name"))
    lname = models.CharField(max_length=30, verbose_name=_("Last Name"), help_text=_("Please Enter your last name"))
    username = models.CharField(max_length=30, unique=True, verbose_name=_("Username"), help_text=_("Please Enter your username"))
 


    def __str__(self):
        return self.username
    
    

class Address(BaseModel):
    """
    Address model belongs to Customers and it contains Country, Province, City, Details and Postal code
    """

    customer = models.ForeignKey(to=Customer, on_delete=models.RESTRICT)

    country_en = models.CharField(max_length=30, default='Iran', verbose_name=_("country in english"),
    help_text=_("Please Enter your country in English(default: Iran)."))

    country_fa = models.CharField(max_length=30, default='Iran', verbose_name=_("country in persian"),
    help_text=_("Please Enter your country in Persian(default: Iran)."))

    province_en = models.CharField(max_length=30, verbose_name=_("province in english"),
    help_text=_("Please Enter your province in English(Tehran, Shiraz, ...)"))

    province_fa = models.CharField(max_length=30, verbose_name=_("province in persian"),
    help_text=_("Please Enter your province in Persian(Tehran, Shiraz, ...)"))

    city_en = models.CharField(max_length=30, verbose_name=_("city in english"), help_text=_("Please Enter your city in English"))

    city_fa = models.CharField(max_length=30, verbose_name=_("city in persian"), help_text=_("Please Enter your city in Persian"))

    detail_en = models.CharField(max_length=255, verbose_name=_("address in english"), 
    help_text=_("Please Enter details of yout address in English(like street, allay and so on...)"))

    detail_fa = models.CharField(max_length=255, verbose_name=_("address in persian"), 
    help_text=_("Please Enter details of yout address in Persian(like street, allay and so on...)"))

    postal_code = models.CharField(max_length=10, unique=True, verbose_name=_("Zip code"), 
    validators=[Validators.check_postal_code], help_text=_("Please Enter your zip code"))

    def __str__(self):
        return f"Country: {self.country_en} Province: {self.province_en} City: {self.city_en}"
    