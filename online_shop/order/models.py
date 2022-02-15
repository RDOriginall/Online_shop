from django.db import models
from django.utils.translation import ugettext_lazy as _
from core import BaseModel
from product import Discount
# Create your models here.

class OffCode(Discount):
    """
    Off code is a code that makes a total discount on Order model
    """
    code = models.CharField(max_length=10, unique=True, verbose_name=_("Discount code"),
    help_text=_("Please Enter Off code"))
    users = models.ManyToManyField(to=Customer, related_name="codes", default=None, null=True,
    verbose_name=_("User Off code"), help_text=_("which users have used this code?"))
    


class Order(BaseModel):
    pass



class OrderItem(BaseModel):
    pass