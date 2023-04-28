from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'shipments', views.ShipmentViewSet, basename='shipment')

urlpatterns = [
    path("", views.index, name="index"),
    path("api_auth/", include("rest_framework.urls")),
    path("test/", views.TestView.as_view(), name="test"),
    path("shipment_types/", views.ShipmentTypeListView.as_view(), name="list_shipment_types"),
    path("", include(router.urls)),
]