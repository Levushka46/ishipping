from rest_framework.serializers import Serializer, CharField, ModelSerializer
from .models import Shipment, ShipmentType


class TestObject():
    def __init__(self):
        self.stroka = "Meow"


class TestObjectSerializer(Serializer):
    stroka = CharField()


class ShipmentTypeSerializer(ModelSerializer):
    class Meta:
        model = ShipmentType
        fields = ['id', 'name']
    

class ShipmentSerializer(ModelSerializer):
    shipment_type = CharField(source='shipment_type.name')
    class Meta:
        model = Shipment
        fields = ['id', 'name', 'weight', 'shipment_type', 'worth', 'shipping_cost']