from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import ngettext_lazy


@deconstructible
class MinLengthCustom(BaseValidator):
    message = ngettext_lazy(
        "The username must be a minimum of %(limit_value)d chars",
        "The username must be a minimum of %(limit_value)d chars",
        "limit_value",
    )
    code = "min_length"

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)


def YearValidator(value):
    if 1980 > value or 2049 < value:
        raise ValidationError("Year must be between 1980 and 2049")
