from django.core.exceptions import *
from django.utils.translation import ugettext_lazy as _
import re as r


class Validators:
    """
    Validation for all inputs in all apps and mdels
    """

    PHONE_NUMBER_PATTERN = r"^(09)([0-9]{9})$"
    POSTAL_CODE_PATTERN = r"^([0-9]{10})$"

    
    def start_with_letter(value: str):
        if not value[0].isalpha():
            raise Exception(_("This text should start with Letters"))
        else:
            pass

    
