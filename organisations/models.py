from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


def validate_postcode(postcode):
    if postcode < 0 or postcode > 999999:
        raise ValidationError(
            _("%(value)s is not an even number"),
            params={"value": postcode}
        )


class Organisation(models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    address = models.TextField()
    postcode = models.IntegerField(validators=[validate_postcode])

    @property
    def full_address(self):
        return f'{self.postcode} {self.address}'

    class Meta:
        default_related_name = 'organisations'