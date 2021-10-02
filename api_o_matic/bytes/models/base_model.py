from django.conf import settings
from django.db.models import PROTECT, BooleanField, DateTimeField, ForeignKey, Model
from django.utils.translation import gettext_lazy as _

from api_o_matic.bytes.managers import BaseManager


class BaseModel(Model):
    is_active = BooleanField(_("Is active?"), default=True)
    created_by = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=PROTECT,
    )
    created_at = DateTimeField(_("Created on"), auto_now_add=True)
    updated_at = DateTimeField(_("Last modified on"), auto_now=True)
    objects = BaseManager()

    def delete(self, using=None, keep_parents=False):
        self.is_active = False

    delete.alters_data = True  # type: ignore

    class Meta:
        abstract = True
