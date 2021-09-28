import uuid

from django.db.models import CharField, URLField, UUIDField
from django.utils.translation import gettext_lazy as _

from api_o_matic.bytes.models.base_model import BaseModel


class Source(BaseModel):
    """Source model for Api-o-Matic"""

    TYPE_HTML = "html"
    TYPE_JSON = "json"

    TYPE_CHOICES = (
        (TYPE_HTML, "HTML"),
        (TYPE_JSON, "JSON"),
    )

    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = URLField(_("URL of Source"), blank=False)
    description = CharField(_("Description of Bit"), blank=True, max_length=255)
    type_source = CharField(
        _("Type of Source"), choices=TYPE_CHOICES, max_length=50, blank=False
    )

    def __str__(self):
        return self.url
