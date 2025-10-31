from django.db import models
from apps.masters.models import Item, Vendor

class Inward(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    batch_no = models.CharField(max_length=50)
    date = models.DateField()
    purchase_rate = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Update item quantity on inward
        self.item.quantity += self.quantity
        self.item.save()
        super().save(*args, **kwargs)

class Outward(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Update item quantity on outward
        self.item.quantity -= self.quantity
        self.item.save()
        super().save(*args, **kwargs)

class StockStatement(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    inward_total = models.IntegerField(default=0)
    outward_total = models.IntegerField(default=0)
    closing_stock = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default="Sufficient")
    last_updated = models.DateTimeField(auto_now=True)