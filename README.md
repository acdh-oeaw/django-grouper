Group Django model instances on similar fields

Based on [this tutorial](https://towardsdatascience.com/group-thousands-of-similar-spreadsheet-text-cells-in-seconds-2493b3ce6d8d)

# Installation

1. add `django_grouper` to your `INSTALLED_APPS`
2. add `path("", include("django_grouper.urls"))` to your `urlpatterns`
3. go to `/grouper` and add the param `content_type` to specify which ContentType to group and the params `fields` to specify which fields to group by
