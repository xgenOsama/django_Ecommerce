# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='final_price',
            field=models.DecimalField(default=10.99, max_digits=1000, decimal_places=2),
        ),
        migrations.AddField(
            model_name='order',
            name='sub_total',
            field=models.DecimalField(default=10.99, max_digits=1000, decimal_places=2),
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.DecimalField(default=0.0, max_digits=1000, decimal_places=2),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
