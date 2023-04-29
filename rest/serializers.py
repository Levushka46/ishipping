from rest_framework.serializers import Serializer, CharField, ModelSerializer, IntegerField, DecimalField
from .models import Shipment, ShipmentType
from decimal import Decimal

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


class RegisterShipmentSerializer(ModelSerializer):

    class Meta:
        model = Shipment
        fields = ['id', 'name', 'weight', 'shipment_type', 'worth']
        read_only_fields = ['id']
        extra_kwargs = {
            'weight': {
                'min_value': 0
            },
            'worth': {
                'min_value': Decimal("0.01"), 
                'max_digits': 10,
                'decimal_places': 2
            }
        }