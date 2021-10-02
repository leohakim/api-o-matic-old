from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api_o_matic.bytes.api.serializers.byte import ByteSerializer
from api_o_matic.bytes.models import Byte
from api_o_matic.users.models import User


class ByteViewSet(GenericViewSet):
    serializer_class = ByteSerializer
    queryset = Byte.objects.all()
    lookup_field = "slug"
    permission_classes = (AllowAny,)

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(slug=kwargs["slug"])

    def retrieve(self, request, **kwargs):
        user_input = kwargs.get("user")
        byte_input = kwargs.get("byte")
        if not user_input or not User.objects.filter(username=user_input).exists():
            return Response(
                data={"error": "User does not exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not byte_input or not Byte.objects.filter(slug=byte_input).exists():
            return Response(
                data={"error": "Byte does not exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        byte = Byte.objects.get(slug=byte_input)
        user = User.objects.get(username=user_input)
        if byte.created_by != user:
            return Response(
                data={"error": "This user does not own this byte"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = ByteSerializer(byte, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
