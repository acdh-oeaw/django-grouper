Group Django model instances on similar fields

Based on [this tutorial](https://towardsdatascience.com/group-thousands-of-similar-spreadsheet-text-cells-in-seconds-2493b3ce6d8d)

# Installation

1. add `django_grouper` to your `INSTALLED_APPS`
2. add `path("", include("django_grouper.urls"))` to your `urlpatterns`
3. go to `/grouper` and add the param `group_content_type` to specify which ContentType to group and the params `group_fields` to specify which fields to group by

# Configuration

If you define a `GROUP_FILTER` in you settings, the queryset in the `/grouper` view will be passed through this filter. The filter is expected to
be a callable and will receive the queryset and the request as parameters. This means you can pass the queryset together with the request to a
django-filter filter.
You also need to add a `GROUP_MERGE_FUNCTION` in your settings. This needs to be the string representation of a merge function implemented in your model. 
If you dont set it, grouper expects a function called `merge` function in your model.
If you click on `Merge selected` grouper will call that function on the main object you selected and give it as only attribute a list of objects to merge.
E.g. if you use it on a `Person` model and you add `GROUP_MERGE_FUNCTION = "merge"` to your settings it will call 
`Person.objects.get(pk=MAIN_PK).merge([PERSON_TO_MERGE_A, PERSON_TO_MERGE_B...])`. It expects the merge function to return the merged object.
