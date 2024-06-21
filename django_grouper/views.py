from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView

from .utils import group_queryset


class BaseView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        app_label, model = request.GET.get("content_type", ".").split(".")
        self.django_content_type = get_object_or_404(ContentType, app_label=app_label, model=model)
        return super().dispatch(request, *args, **kwargs)


class Grouper(BaseView):
    template_name = "django_grouper/grouper.html"

    def get_context_data(self, *args, **kwargs):
        fields = self.request.GET.getlist("fields", [])

        ctx = super().get_context_data(*args, **kwargs)
        ctx["content_type"] = self.django_content_type
        ctx["groups"] = group_queryset(self.get_queryset(), fields)
        return ctx

    def get_queryset(self):
        return self.django_content_type.model_class().objects.all()


class Group(BaseView):
    template_name = "django_grouper/group.html"

    def get_context_data(self, *args, **kwargs):
        ids = self.request.GET.getlist("ids", [])

        ctx = super().get_context_data(*args, **kwargs)
        ctx["content_type"] = self.django_content_type
        ctx["title"] = self.request.GET.get("group_title")
        ctx["object_list"] = self.django_content_type.model_class().objects.filter(pk__in=ids)
        return ctx

    def post(self, request, *args, **kwargs):
        ctx = self.get_context_data()
        ctx["merged_ids"] = []
        for merge_id in request.POST.getlist("to_merge"):
            ctx["merged_ids"].append(merge_id)
        return self.render_to_response(ctx)
