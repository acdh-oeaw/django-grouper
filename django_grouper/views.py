from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.template.loader import select_template
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect


from .utils import group_queryset
from django_grouper.signals import trigger_merge


class BaseView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        app_label, model = request.GET.get("group_content_type", ".").split(".")
        self.django_content_type = get_object_or_404(
            ContentType, app_label=app_label, model=model
        )
        return super().dispatch(request, *args, **kwargs)


class Grouper(BaseView):
    template_name = "django_grouper/grouper.html"

    def get_context_data(self, *args, **kwargs):
        fields = self.request.GET.getlist("group_fields", [])

        ctx = super().get_context_data(*args, **kwargs)
        ctx["content_type"] = self.django_content_type
        ctx["groups"] = group_queryset(self.get_queryset(), fields)
        # these are the template names that are used in apis
        ctx["base_template"] = select_template(["webpage/base.html", "base.html"])
        return ctx

    def get_queryset(self):
        qs = self.django_content_type.model_class().objects.all()
        if hasattr(settings, "GROUP_FILTER"):
            qs = settings.GROUP_FILTER(qs, self.request)
        return qs


class Group(BaseView):
    template_name = "django_grouper/group.html"

    def get_context_data(self, *args, **kwargs):
        ids = self.request.GET.getlist("ids", [])

        ctx = super().get_context_data(*args, **kwargs)
        ctx["content_type"] = self.django_content_type
        ctx["title"] = self.request.GET.get("group_title")
        ctx["object_list"] = self.django_content_type.model_class().objects.filter(
            pk__in=ids
        )
        # these are the template names that are used in apis
        ctx["base_template"] = select_template(["webpage/base.html", "base.html"])
        return ctx

    def post(self, request, *args, **kwargs):
        primary = request.POST.get("primary", None)
        to_merge = request.POST.get("to_merge", None)
        if primary and to_merge:
            model = self.django_content_type.model_class()
            primary = model.objects.get(pk=primary)
            secondaries = [
                get_object_or_404(model, pk=pk)
                for pk in request.POST.getlist("to_merge")
            ]
            trigger_merge.send(self, primary=primary, secondaries=secondaries)
            return HttpResponseRedirect(primary.get_absolute_url())
        raise ValidationError(
            "Expected `primary` and `to_merge` values, but could not find them."
        )
