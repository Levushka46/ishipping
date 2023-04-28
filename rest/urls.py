from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.TestView.as_view(), name="test"),
    path("shipment_types/", views.ShipmentTypeListView.as_view(), name="list_shipment_types"),
    path("api_auth/", include("rest_framework.urls")),
]