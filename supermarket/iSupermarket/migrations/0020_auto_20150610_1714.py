# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iSupermarket', '0019_auto_20150610_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 17, 14, 22, 999772, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sucursalreview',
            name='rating',
            field=models.PositiveSmallIntegerField(default=3, verbose_name=b'ratings (stars)', choices=[(b'5', b'5'), (b'4', b'4'), (b'3', b'3'), (b'2', b'2'), (b'1', b'1')]),
        ),
    ]
