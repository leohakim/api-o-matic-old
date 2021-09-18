from factory import Iterator, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

from api_o_matic.bytes.models.bit import Bit
from api_o_matic.bytes.models.byte import Byte
from api_o_matic.bytes.models.source import Source
from api_o_matic.tests.users.factories import UserFactory

faker = Faker("bs_BA")


class SourceFactory(DjangoModelFactory):
    url = faker.uri()
    description = faker.text
    type_source = Iterator([Source.TYPE_HTML, Source.TYPE_JSON])
    created_by = SubFactory(UserFactory)

    class Meta:
        model = Source
        django_get_or_create = ["url"]


class BitFactory(DjangoModelFactory):
    name = faker.name()
    type_bit = Iterator(
        [Bit.TYPE_STRING, Bit.TYPE_NUMBER, Bit.TYPE_DATE, Bit.TYPE_DATETIME]
    )
    path = faker.address()
    value = faker.text()
    source = SubFactory(SourceFactory)
    created_by = SubFactory(UserFactory)

    class Meta:
        model = Bit
        django_get_or_create = ["name"]


class ByteFactory(DjangoModelFactory):
    name = faker.name()
    description = faker.text
    created_by = SubFactory(UserFactory)

    class Meta:
        model = Byte
        django_get_or_create = ["name"]
