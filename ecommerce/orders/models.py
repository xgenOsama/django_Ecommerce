from django.contrib.auth.models import User
from django.db import models
from carts.models import Cart


# Create your models here.

STATUS_CHOICHES = (
    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished"),
)


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    order_id = models.CharField(max_length=120, default='ABC', unique=True)
    cart = models.ForeignKey(Cart)
    status = models.CharField(max_length=120, choices=STATUS_CHOICHES, default="Started")
    sub_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    tax = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    final_price = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __unicode__(self):
        return self.order_id
