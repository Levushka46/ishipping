from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import ParseError
from rest_framework.mixins import CreateModelMixin
from .serializers import TestObject, TestObjectSerializer, ShipmentTypeSerializer, ShipmentSerializer, RegisterShipmentSerializer
from .models import ShipmentType, Shipment
from taskqueue.tasks import calc_shipping_cost

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class TestView(APIView):

    def get(self, *args, **kwargs):
        instance = TestObject()
        serializer = TestObjectSerializer(instance)
        calc_shipping_cost.apply_async()
        return Response(self.request.session)


class ShipmentTypeListView(ListAPIView):
    queryset = ShipmentType.objects.all()
    serializer_class = ShipmentTypeSerializer


class ShipmentViewSet(CreateModelMixin, ReadOnlyModelViewSet):
    serializer_class = ShipmentSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = Shipment.objects.filter(id__in=self.request.session.get('shipment_ids', []))
        shipment_type = self.request.query_params.get('shipment_type')
        shipping_cost = self.request.query_params.get('shipping_cost')

        if shipment_type is not None:
            try:
                queryset = queryset.filter(shipment_type=int(shipment_type))
            except ValueError:
                raise ParseError('shipment_type should be integer')

        if shipping_cost is not None:
            try:
                if shipping_cost == 'True':
                    queryset = queryset.filter(shipping_cost__isnull=False)
                elif shipping_cost == 'False':
                    queryset = queryset.filter(shipping_cost__isnull=True)
            except ValueError:
                raise ParseError('shipping_cost should be bool (True or False)')
        return queryset

    def get_serializer_class(self):
        if self.action == "create":
            return RegisterShipmentSerializer

        return super().get_serializer_class()
    
    def perform_create(self, serializer):
        instance = serializer.save()
        shipment_ids = self.request.session.get('shipment_ids', [])
        shipment_ids.append(instance.id)
        self.request.session['shipment_ids'] = shipment_ids