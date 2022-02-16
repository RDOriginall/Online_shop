from django.core.exceptions import *
from django.utils.translation import ugettext_lazy as _
import re as r


class Validators:
    """
    Validation for all inputs in all apps and mdels
    """

    PHONE_NUMBER_PATTERN = r"^(09)([0-9]{9})$"
    POSTAL_CODE_PATTERN = r"^([0-9]{10})$"

    
    def start_with_letter(self, value: str):
        """
        This method checks if the input is starting with a letter or not
        """
        if not value[0].isalpha():
            raise Exception(_("This text should start with Letters"))
        else:
            pass

    
    
    def check_phone_number(self, phone: str):
        """
        Validation for phone numbers, EXAMPLE: 09123456789
        """

        if r.search(self.PHONE_NUMBER_PATTERN, phone):
            pass
        else:
            raise ValidationError(_("Wrong input, correct input example: 09123456789"))


    
    def check_postal_code(self, code: str):
        """
        Validatin for postal code
        """

        if r.search(self.POSTAL_CODE_PATTERN, code):
            pass
        else:
            raise ValidationError(_("postal code must be 10 digits"))