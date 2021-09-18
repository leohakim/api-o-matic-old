from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BytesConfig(AppConfig):
    name = "api_o_matic.bytes"
    verbose_name = _("Bytes")

    def ready(self):
        try:
            import api_o_matic.bytes.signals  # noqa F401
        except ImportError:
            pass
