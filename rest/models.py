from django.db import models


class ShipmentType(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name


class Shipment(models.Model):
    name = models.CharField(max_length=256)
    weight = models.IntegerField()
    shipment_type = models.ForeignKey(ShipmentType, on_delete=models.CASCADE)
    worth = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cost = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)