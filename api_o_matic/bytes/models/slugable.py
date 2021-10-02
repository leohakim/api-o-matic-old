from django.db.models import Model, SlugField
from django.template.defaultfilters import slugify


class Slugable(Model):
    slug = SlugField(null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
