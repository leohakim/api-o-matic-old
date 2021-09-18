from django.conf import settings
from django.db.models import PROTECT, BooleanField, DateTimeField, ForeignKey, Model


class BaseModel(Model):
    is_active = BooleanField("is active?", default=True)
    created_by = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=PROTECT,
    )
    created_at = DateTimeField("created on", auto_now_add=True)
    updated_at = DateTimeField("last modified on", auto_now=True)

    def delete(self, using=None, keep_parents=False):
        self.is_active = False

    delete.alters_data = True  # type: ignore

    class Meta:
        abstract = True
