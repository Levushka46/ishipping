from celery import shared_task
from rest.models import Shipment, ShipmentType
from .currency import fetch_currency
from .cache import get_usd_rub, set_usd_rub

@shared_task
def calc_shipping_cost():
    if not (usd_rub := get_usd_rub()):
        usd_rub = fetch_currency('USD') 
        set_usd_rub(usd_rub)
    
    no_shipping_cost = Shipment.objects.filter(shipping_cost__isnull=True)
    for obj in no_shipping_cost:
        obj.shipping_cost = (obj.weight/1000*0.5+float(obj.worth)*0.01)*usd_rub
        obj.save()