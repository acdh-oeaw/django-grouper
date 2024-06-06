from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView

from .utils import group_queryset


class Grouper(TemplateView):
    template_name = "django_grouper/grouper.html"

    def get_context_data(self, *args, **kwargs):
        fields = self.request.GET.getlist("fields", [])
        app_label, model = self.request.GET.get("content_type", ".").split(".")
        content_type = get_object_or_404(ContentType, app_label=app_label, model=model)

        ctx = super().get_context_data(*args, **kwargs)
        ctx["content_type"] = content_type
        ctx["groups"] = group_queryset(content_type.model_class().objects.all(), fields)
        return ctx
