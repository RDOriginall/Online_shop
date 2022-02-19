from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel
from product.models import Discount, Product, OffCode
from django.core.validators import MinValueValidator
from customer.models import Customer, Address
# Create your models here.


class Order(BaseModel):
    """
    Order model is kinda the cart or the 'Receipt' of total OrderItems
    """
    total_price = models.FloatField(verbose_name=_("Total price"), validators=[MinValueValidator(0)])
    final_price = models.FloatField(verbose_name=_("Final proce"), validators=[MinValueValidator(0)])
    off_code = models.ForeignKey(to=OffCode, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(to=Customer, verbose_name=_("customer cart"), on_delete=models.RESTRICT)
    address = models.ForeignKey(to=Address, on_delete=models.RESTRICT, verbose_name=_("Address"), help_text=_("Please select your address"))
    status = models.CharField(max_length=1, default='U', verbose_name=_("Order Status"),
    choices=[('P', _('Paid')), ('U', _('Unpaid')), ('C', _('Canceled'))])

    class Meta:
        unique_together = [['off_code', 'customer']] # Just once Time Use from OffCode



class OrderItem(BaseModel):
    """
    OrderItem model contains Items that the client wants to order
    """
    order = models.ForeignKey(to=Order, on_delete=models.RESTRICT, related_name="items", 
    verbose_name=_("Receipt"), help_text=_("Please select your order"))
    product = models.ForeignKey(to=Product, on_delete=models.RESTRICT, verbose_name=_("Product name"),
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