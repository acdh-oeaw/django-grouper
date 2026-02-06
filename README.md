Group Django model instances based on similar fields

# Installation

1. add `django_grouper` to your `INSTALLED_APPS`
2. add `path("", include("django_grouper.urls"))` to your `urlpatterns`
3. go to `/grouper` and add the param `group_content_type` to specify which ContentType to group and the params `group_fields` to specify which fields to group by

# Configuration

If you define a `GROUP_FILTER` in you settings, the queryset in the `/grouper` view will be passed through this filter. The filter is expected to
be a callable and will receive the queryset and the request as parameters. This means you can pass the queryset together with the request to a
django-filter filter.

The `/group` view lets you select which objects of a list should be merged. If
you double click an object, it will become the primary, a single click marks an
object as secondary. There can be one primary and multiple secondaries. The
primary and the list of secondaries are then passed to the `trigger_merge`
signal. You can use this method to implement a custom merge method.

```
from django_grouper.signals import trigger_merge


@receiver(trigger_merge)
def react_on_merge_trigger(sender, primary, secondaries, **kwargs):
    primary.merge(secondaries)
```
