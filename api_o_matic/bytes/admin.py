from django.contrib import admin

from api_o_matic.bytes.models import Bit, Byte, Source


@admin.register(Bit)
class BitAdmin(admin.ModelAdmin):
    def time_seconds(self, obj):
        return obj.updated_at.strftime("%d-%m-%y %H:%M:%S")

    time_seconds.admin_order_field = "updated_at"
    time_seconds.short_description = "Last Update"

    list_display = (
        "id",
        "name",
        "value",
        "time_seconds",
        "source",
        "is_active",
        "description",
        "type_bit",
        "path",
        "created_at",
    )
    search_fields = ["name", "description"]


@admin.register(Byte)
class ByteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "show_bits",
        "public",
        "created_at",
        "is_active",
    )
    search_fields = ["name", "description"]
    prepopulated_fields = {"slug": ("name",)}

    def show_bits(self, byte):
        return (
            "[" + "".join([_.name for _ in byte.bits.all()]) + "]"
        )  # pragma: no cover <--

    show_bits.short_description = "Bits"  # type: ignore


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "url",
        "description",
        "type_source",
        "created_at",
        "is_active",
    )
    search_fields = ["url", "description"]
