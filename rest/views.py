from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import ParseError
from .serializers import TestObject, TestObjectSerializer, ShipmentTypeSerializer, ShipmentSerializer
from .models import ShipmentType, Shipment

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class TestView(APIView):

    def get(self, *args, **kwargs):
        instance = TestObject()
        serializer = TestObjectSerializer(instance)
        return Response(serializer.data)


class ShipmentTypeListView(ListAPIView):
    queryset = ShipmentType.objects.all()
    serializer_class = ShipmentTypeSerializer


class ShipmentViewSet(ReadOnlyModelViewSet):
    serializer_class = ShipmentSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Shipment.objects.all()
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