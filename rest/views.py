from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TestObject, TestObjectSerializer, ShipmentTypeSerializer
from .models import ShipmentType, Shipment

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class TestView(APIView):

    def get(self, *args, **kwargs):
        instance = TestObject()
        serializer = TestObjectSerializer(instance)
        return Response(serializer.data)


class ShipmentTypeListView(APIView):

    def get(self, *args, **kwargs):
        shipment_types = ShipmentType.objects.all()
        serializer = ShipmentTypeSerializer(shipment_types, many=True)
        return Response(serializer.data)