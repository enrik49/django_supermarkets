# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iSupermarket', '0018_auto_20150610_1612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sucursalreview',
            old_name='restaurant',
            new_name='sucursal',
        ),
        migrations.AlterField(
            model_name='client',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 16, 48, 50, 237669, tzinfo=utc)),
        ),
    ]
