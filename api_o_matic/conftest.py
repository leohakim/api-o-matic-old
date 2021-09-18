import pytest

from api_o_matic.bytes.models.bit import Bit
from api_o_matic.bytes.models.byte import Byte
from api_o_matic.bytes.models.source import Source
from api_o_matic.tests.bytes.factories import BitFactory, ByteFactory, SourceFactory
from api_o_matic.tests.users.factories import UserFactory
from api_o_matic.users.models import User


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def byte() -> Byte:
    return ByteFactory()


@pytest.fixture
def bit() -> Bit:
    return BitFactory()


@pytest.fixture
def source() -> Source:
    return SourceFactory()
