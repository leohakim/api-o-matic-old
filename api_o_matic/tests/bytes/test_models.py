import pytest

from api_o_matic.bytes.models.bit import Bit
from api_o_matic.bytes.models.byte import Byte
from api_o_matic.bytes.models.source import Source

pytestmark = pytest.mark.django_db


def test_bit_return_name(bit: Bit):
    assert bit.__str__() == f"{bit.name}"


def test_byte_return_name(byte: Byte):
    assert byte.__str__() == f"{byte.name}"


def test_source_return_url(source: Source):
    assert source.__str__() == f"{source.url}"


def test_when_delete_bit_then_is_active_false(bit: Bit):
    bit.delete()
    assert bit.is_active is False
