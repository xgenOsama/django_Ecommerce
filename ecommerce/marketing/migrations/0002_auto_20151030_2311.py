# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marketingmessage',
            old_name='end_data',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='marketingmessage',
            old_name='start_data',
            new_name='start_date',
        ),
    ]
