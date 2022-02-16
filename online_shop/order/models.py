from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel
from product.models import Discount, Product
from django.core.validators import MinValueValidator
from customer.models import Customer
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
    """
    Order model is kinda the cart or the 'Receipt' of total OrderItems
    """
    total_price = models.FloatField(verbose_name=_("Total price"), validators=[MinValueValidator(0)])
    final_price = models.FloatField(verbose_name=_("Final proce"), validators=[MinValueValidator(0)])
    customer = models.ForeignKey(to=Customer, verbose_name=_("customer cart"), on_delete=models.CASCADE)
    status = models.CharField(max_length=1, default='U', verbose_name=_("Order Status"),
    choices=[('P', _('Paid')), ('U', _('Unpaid')), ('C', _('Canceled'))])



class OrderItem(BaseModel):
    """
    OrderItem model contains Items that the client wants to order
    """
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name="items", 
    verbose_name=_("Receipt"), help_text=_("Please select your order"))
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name=_("Product name"),
    help_text=_("Please select Product Item to add"))
    count = models.PositiveIntegerField(default=1, verbose_name=_("number of Order Items"), 
    validators=[MinValueValidator(1)], help_text=_("How many Items would you like to order?"))
    

    @property
    def item_total_price(self):
        """
        This method calculates total price of an Item that client wants to order
        by considering the number of that item considering discount
        """

        return self.count * self.product.final_price()