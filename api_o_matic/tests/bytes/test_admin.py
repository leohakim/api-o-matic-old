import pytest
from django.urls import reverse

from api_o_matic.bytes.models import Bit, Byte

from .factories import BitFactory, ByteFactory

pytestmark = pytest.mark.django_db


class TestBitAdmin:
    def test_changelist(self, admin_client):
        url = reverse("admin:bytes_bit_changelist")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_search(self, admin_client):
        url = reverse("admin:bytes_bit_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == 200

    def test_view_bit(self, admin_client):
        BitFactory(name="test")
        bit = Bit.objects.get(name="test")
        url = reverse("admin:bytes_bit_change", kwargs={"object_id": bit.pk})
        response = admin_client.get(url)
        assert response.status_code == 200


class TestByteAdmin:
    def test_changelist(self, admin_client):
        url = reverse("admin:bytes_byte_changelist")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_search(self, admin_client):
        url = reverse("admin:bytes_byte_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == 200

    def test_view_byte(self, admin_client):
        ByteFactory(name="test")
        byte = Byte.objects.get(name="test")
        url = reverse("admin:bytes_byte_change", kwargs={"object_id": byte.pk})
        response = admin_client.get(url)
        assert response.status_code == 200
