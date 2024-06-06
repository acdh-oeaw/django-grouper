from django.urls import path

from . import views

urlpatterns = [path("grouper/", views.Grouper.as_view(), name="grouper")]
