from rest_framework import serializers

from api_o_matic.bytes.models import Bit, Byte


class BitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bit
        fields = ["name", "description", "type_bit", "value", "updated_at"]

        extra_kwargs = {"url": {"view_name": "api:bit-detail", "lookup_field": "name"}}


class ByteSerializer(serializers.ModelSerializer):
    bits = BitSerializer(many=True)

    class Meta:
        model = Byte
        fields = ["name", "description", "bits"]

        extra_kwargs = {"url": {"view_name": "api:byte-detail", "lookup_field": "name"}}
