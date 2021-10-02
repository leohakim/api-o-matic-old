from django.db.models import Manager


class BaseManager(Manager):
    """Base Manager for Api-o-Matic"""

    def active(self):
        return self.filter(is_active=True)
