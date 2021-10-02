from django.http import HttpResponseBadRequest
from django.views.generic import TemplateView

from api_o_matic.bytes.models import Byte
from api_o_matic.users.models import User


class HomeView(TemplateView):
    template_name = "pages/home.html"
    extra_context = {
        "most_visited_bytes": Byte.objects.active().order_by("-created_at")
    }


class UserBytesView(TemplateView):
    template_name = "pages/user_bytes.html"

    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(name=kwargs["user"])
            byte = Byte.objects.get(slug=kwargs["byte"], created_by=user)
        except (AttributeError, User.DoesNotExist, Byte.DoesNotExist) as error:
            return HttpResponseBadRequest(f"{error}")
        context = self.get_context_data(**kwargs)
        context["bits"] = byte.bits.all()
        return self.render_to_response(context)
