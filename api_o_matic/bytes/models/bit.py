import uuid

from django.db.models import PROTECT, CharField, ForeignKey, UUIDField
from django.utils.translation import gettext_lazy as _

from api_o_matic.bytes.models.base_model import BaseModel
from api_o_matic.bytes.models.source import Source


class Bit(BaseModel):
    """Bit model for Api-o-Matic"""

    TYPE_STRING = "string"
    TYPE_NUMBER = "number"
    TYPE_DATE = "date"
    TYPE_DATETIME = "datetime"

    TYPE_CHOICES = (
        (TYPE_STRING, "String"),
        (TYPE_NUMBER, "Number"),
        (TYPE_DATE, "Date"),
        (TYPE_DATETIME, "DateTime"),
    )

    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(_("Name of Bit"), blank=False, max_length=255)
    description = CharField(_("Description of Bit"), blank=True, max_length=255)
    type_bit = CharField(
        _("Type of Bit"), choices=TYPE_CHOICES, max_length=50, blank=False
    )
    path = CharField(_("Path of Bit"), max_length=250, blank=False)
    value = CharField(_("Value of Bit"), max_length=250, blank=True)
    source = ForeignKey(Source, on_delete=PROTECT)

    def __str__(self):
        return self.name
