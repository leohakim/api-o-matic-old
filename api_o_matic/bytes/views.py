from django.http import HttpResponseBadRequest
from django.views.generic import TemplateView

from api_o_matic.bytes.models import Bit, Byte
from api_o_matic.users.models import User


class HomeView(TemplateView):
    template_name = "pages/home.html"
    users = User.objects.filter(is_active=True)[:10]
    ranking = dict()
    for user in users:
        bits_per_user = Bit.objects.active().filter(created_by=user).count()
        ranking[user.username] = bits_per_user

    sort_by_value = dict(
        sorted(ranking.items(), key=lambda item: item[1], reverse=True)
    )

    extra_context = {
        "users": sort_by_value,
        "most_visited_bytes": Byte.objects.active().order_by("-created_at"),
    }


class UserBytesDetailView(TemplateView):
    template_name = "pages/user_bytes_detail.html"

    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(username=kwargs["user"])
            byte = Byte.objects.get(slug=kwargs["byte"], created_by=user)
        except (AttributeError, User.DoesNotExist, Byte.DoesNotExist) as error:
            return HttpResponseBadRequest(f"{error}")
        context = self.get_context_data(**kwargs)
        context["bits"] = byte.bits.all()

        return self.render_to_response(context)


class UserBytesView(TemplateView):
    template_name = "pages/user_bytes.html"

    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(username=kwargs["user"])
            bytes = Byte.objects.filter(created_by=user)
        except (AttributeError, User.DoesNotExist) as error:
            return HttpResponseBadRequest(f"{error}")
        context = self.get_context_data(**kwargs)
        context["bytes"] = bytes

        return self.render_to_response(context)
