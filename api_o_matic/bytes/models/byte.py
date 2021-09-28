import uuid

from django.db.models import BooleanField, CharField, ManyToManyField, UUIDField
from django.utils.translation import gettext_lazy as _

from api_o_matic.bytes.models.base_model import BaseModel
from api_o_matic.bytes.models.bit import Bit


class Byte(BaseModel):
    """Byte model for Api-o-Matic"""

    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(_("Name of Byte"), blank=False, max_length=255)
    description = CharField(_("Description of Byte"), blank=True, max_length=255)
    bits = ManyToManyField(Bit, blank=True)
    public = BooleanField(default=True)

    def __str__(self):
        return self.name
