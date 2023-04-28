from django.contrib import admin
from .models import Shipment, ShipmentType

admin.site.register(Shipment) 
admin.site.register(ShipmentType)
# Register your models here.
